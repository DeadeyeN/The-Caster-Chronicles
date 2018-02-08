#! python3

'''
	Trawls the Caster Chronicles database for card information and outputs as an XML for use in Cockatrice.
	Author: Stefan Letica
	Version: 1.0
	Latest update: 2/8/2018
'''
import sys
import lxml.etree as ET
from bs4 import BeautifulSoup
from urllib.request import urlopen

'''
	Holds the overarching card list
	0 - Card name
	1 - 2D array of card set and associated picture url
	2 - Card type
	3 - Card Attribute
	4 - Array of effects as strings
	5 - Card Cost or Level (if needed)
	6 - (if needed) ATK/DEF
	7 - (if needed) race and trait
'''
cardList = []

'''
	Holds the overarching set list
	0 - Set code
	1 - Set name
	2 - Set type
	3 - Set release date
'''
setList = []

'''
	input is the color code of the color in the horizontal bar below the card name
	returns the name of the attribute associated with that color
'''
def getAttribute(input):
	if input == "#ff0000,#ff0000":
		return "Ignus"
	elif input == "#0000ff,#0000ff":
		return "Aqua"
	elif input == "#008000,#008000":
		return "Silva"
	elif input == "#ff1493,#ff1493":
		return "Aes"
	elif input == "#ffa500,#ffa500":
		return "Luna"
	elif input == "#800080,#800080":
		return "Terra"
	elif input == "#ffd700,#ffd700":
		return "Solis"
	elif input == "#808080,#808080":
		return "Soulbond"

'''
	a is the number of the first url of the set
	b is the number of the last url of the set
	setCode is the set code that you would like to associate with these cards
	Iterates through the given set of URLs and adds the relevant data to the array of cards
'''
def trawlSet(a, b, setCode):

	#iterate over the set list
	for i in range(a,b+1):	
	
		#open the url
		dl = urlopen('http://en.caster-chronicle-tcg.com/card/' + str(i)).read()
		
		#read the url as an xml file
		card = BeautifulSoup(dl, "lxml")
		
		#extract the name, pic url, type, and attribute
		name = card.find(class_="line-heading-gradient").string;
		picURL = card.find(class_ = "ps-gallery").find("img")['src']
		type = card.find(class_ = "prop-label", text="Type").parent.find(class_="prop-value").string
		attribute = getAttribute(card.find(class_ = "line-heading-gradient")['data-colors'])
		
		#extract the card level/cost if needed
		if (type == "Caster") or (type == "Servant") or (type == "Conjure") or type == "Barrier":
			cost = "".join(card.find(class_ = "prop-label", text="Cost/Level").parent.find(class_ = "prop-value").stripped_strings)
			
			#if it's a caster card, add its cost to its name
			if type == "Caster":
				name = name + " Lv" + cost
		
		#extract the atk/def and race of a servant card
		if type == "Servant" or type == "Soul Bond Servant":
			atkdef = card.find(class_ = "prop-label", text="ATK/DEF").parent.find(class_ = "prop-value").stripped_strings
			race = card.find(class_ = "prop-label", text="Race and Trait").parent.find(class_ = "prop-value").string
			s = "".join(atkdef).split(" / ")
			s[0] = str(int(s[0]) // 100)
			s[1] = str(int(s[1]) // 100)	
			atkdef = s[0] + "/" + s[1]	
			
		#search the database for duplicates and add extra printings if necessary
		found = False
		for c in cardList:
			if c[0] == name:
				c[1].append([setCode, picURL])
				found=True
				break
		if found == True:
			continue
				
		#initialize the array of card info
		add = [name, [[setCode, picURL]], type, attribute, []]	
		  
		#retrieve the card text and strip it of useless tags
		for t in card.find(class_ = "line-heading", text="Card Text").parent.find('section').stripped_strings:
			if (t != "Automatic") and (t != "Activate") and (t != "Continuous"):
				add[4].append(t)

		#append necessary info to the card info array
		if type == "Caster" or type == "Servant" or type == "Conjure" or type == "Barrier":
			add.append(cost)
		if type == "Servant" or type == "Soul Bond Servant":
			add.append(atkdef)
			add.append(race)
		
		#add the newly retrieved card to the array of cards
		cardList.append(add)

#SD01
setList.append(['SD01', 'Starter Deck [Wings of Anger]', 'Starter', '2017-10-20'])
trawlSet(358,378,'SD01')

#SD02
setList.append(['SD02', 'Starter Deck [Arrogant Swallowtail]', 'Starter', '2017-10-20'])
trawlSet(379,400,'SD02')

#BP01
setList.append(['BP01', 'Booster Pack Vol. 1 [The Magic Battle Begins]', 'Expansion', '2017-10-20'])
trawlSet(630,819,'BP01')

#BP01S
setList.append(['BP01S', 'Booster Pack Vol. 1 [The Magic Battle Begins] Secret Rare Cards', 'Special', '2017-10-20'])
trawlSet(820,823,'BP01S')

#BP02
setList.append(['BP02', 'Booster Pack Vol. 2 [πth Dimension Battle Royale]', 'Expansion', '2018-02-09'])
trawlSet(530,607,'BP02')
trawlSet(616,629,'BP02')

#PR
setList.append(['PR', 'The Caster Chronicles Promo Cards', 'Promo', '2018-02-09'])
trawlSet(162,162,'PR')
trawlSet(416,416,'PR')

#create the tree
root = ET.Element("cockatrice_carddatabase", version="3")
sets = ET.SubElement(root, "sets")

#add the sets
for s in setList:
	set = ET.SubElement(sets, "set")
	name = ET.SubElement(set, "name")
	name.text = s[0];
	longname = ET.SubElement(set, "longname")
	longname.text = s[1];
	settype = ET.SubElement(set, "settype")
	settype.text = s[2];
	releasedate = ET.SubElement(set, "releasedate")
	releasedate.text = s[3];

#add the coin set
set = ET.SubElement(sets, "set")
name = ET.SubElement(set, "name")
name.text = "TCCB"
longname = ET.SubElement(set, "longname")
longname.text = "The Caster Chronicles Base"
settype = ET.SubElement(set, "settype")
settype.text = "Core"
releasedate = ET.SubElement(set, "releasedate")
releasedate.text = "2017-10-20"

#create the cards
cards = ET.SubElement(root, "cards")

#add the coin
thecoin = ET.SubElement(cards, "card")
name = ET.SubElement(thecoin, "name")
name.text = "The Coin"
set = ET.SubElement(thecoin, "set", picURL="https://i.imgur.com/7783OBp.png")
set.text = "TCCB"
color = ET.SubElement(thecoin, "color")
cmc = ET.SubElement(thecoin, "cmc")
cmc.text="0"
type = ET.SubElement(thecoin, "type")
tablerow = ET.SubElement(thecoin, "tablerow")
tablerow.text = "0"
text = ET.SubElement(thecoin, "text")
text.text = "Banish this card: Produce [1]. Play this ability only from your caster zone."
token = ET.SubElement(thecoin, "token")
token.text = "1"


#add the cards
for c in cardList:
	card = ET.SubElement(cards, "card")
	name = ET.SubElement(card, "name")
	name.text = c[0]
	for s in c[1]:
		set = ET.SubElement(card, "set", picURL=s[1])
		set.text = s[0]
	
	#for each type, add the necessary XML tags
	if c[2] == "Caster":
		color = ET.SubElement(card, "color")
		color.text = c[3]
		manacost = ET.SubElement(card, "manacost")
		cmc = ET.SubElement(card, "cmc")
		type = ET.SubElement(card, "type")
		type.text = c[2]
		tablerow = ET.SubElement(card, "tablerow")
		tablerow.text = "0"
		text = ET.SubElement(card, "text")
		text.text = "\n".join(c[4])
	elif c[2] == "Servant":
		color = ET.SubElement(card, "color")
		color.text = c[3]
		manacost = ET.SubElement(card, "manacost")
		manacost.text = c[5]
		cmc = ET.SubElement(card, "cmc")
		cmc.text = c[5]
		type = ET.SubElement(card, "type")
		type.text = c[2] + " - " + c[7]
		pt = ET.SubElement(card, "pt")
		pt.text = c[6]
		tablerow = ET.SubElement(card, "tablerow")
		tablerow.text = "3"
		text = ET.SubElement(card, "text")
		text.text = "\n".join(c[4])
	elif c[2] == "Conjure" or c[2] == "Barrier":
		color = ET.SubElement(card, "color")
		color.text = c[3]
		manacost = ET.SubElement(card, "manacost")
		manacost.text = c[5]
		cmc = ET.SubElement(card, "cmc")
		cmc.text = c[5]
		type = ET.SubElement(card, "type")
		type.text = c[2]
		tablerow = ET.SubElement(card, "tablerow")
		tablerow.text = "3"
		text = ET.SubElement(card, "text")
		text.text = "\n".join(c[4])
	elif c[2] == "Soul Bond Servant":
		color = ET.SubElement(card, "color")
		color.text = c[3]
		manacost = ET.SubElement(card, "manacost")
		cmc = ET.SubElement(card, "cmc")
		type = ET.SubElement(card, "type")
		type.text = c[2] + " - " + c[6]
		pt = ET.SubElement(card, "pt")
		pt.text = c[5]
		tablerow = ET.SubElement(card, "tablerow")
		tablerow.text = "3"
		text = ET.SubElement(card, "text")
		text.text = "\n".join(c[4])
	else:
		print(c[2])
		print("You done fucked up, A-A-ron!")
#print out the tree		
tree = ET.ElementTree(root)
tree.write('The Caster Chronicles TCG.xml', encoding='UTF8', method='xml', pretty_print=True, xml_declaration=True)

