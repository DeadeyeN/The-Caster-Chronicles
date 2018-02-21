# The-Caster-Chronicles

## Introduction
Welcome to The Caster Chronicles! This repository contains everything you'll need to play [The Caster Chronicles](http://en.caster-chronicle-tcg.com/) on the program [Cockatrice](https://cockatrice.github.io/). Cockatrice is a program developed in C++ and QT5 for playing Magic: the Gathering by 
a set of awesome developers. The documentation for their program is very robust, and you can learn everything you need to know about it by following the provided link. Thus, I'll only be giving the basic instructions and some tips and tricks in this guide.

Have an issue with this page or the Casters-specific parts of the implementation *(incorrect card text, etc.)*? [Submit a ticket!](https://github.com/DeadeyeN/The-Caster-Chronicles/issues/new)

*Special thanks to my friends Mattaiyah and Enhaloed for helping to re-teach me Python.*

## Installation instructions
This installation guide assumes basic computer literacy and a system without Cockatrice installed.

1. Install Cockatrice for your given system, following all on-screen prompts. 
2. Download this repository and unzip it to a location of your choice.
3. In your file explorer, navigate to AppData/Local/Cockatrice/Cockatrice. *(Hint: If you don't know how to find your AppData folder, go to the address bar of your file explorer and type %AppData%. This takes you to AppData/Roaming. Go up one level and you'll find yourself in AppData, and you should be able to navigate from there.)*
4. Drag the `customsets` and `themes` folders of the unzipped repository into the Cockatrice folder. If you already have these folders created, merge the contents.
5. Open Cockatrice and follow any prompts that it gives to enable sets. If you don't see any Casters cards in the card list, restart Cockatrice.
6. In the settings menu (Cockatrice -> Settings), in the "Appearance" tab, select Casters in the theme dropdown.
7. In the Edit Sets menu (Card Database -> Edit sets), make sure that all of the Caster Chronicles sets are enabled. If you prefer artwork from a certain set, the card database finds card images from the topmost set in the list.

You're done! Restart Cockatrice if needed, then start building and playing!

## Using Cockatrice for The Caster Chronicles
Here are some gameplay tips and tricks to help your game go smoothly and effectively.

1. To place a card facedown on the field, hold `Shift` as you drag the card from whatever zone it's in to the field. For example, as you place orbs at the beginning of the game, hold `Shift` and drag seven cards to the bottom row of your field.
2. Double-clicking a card will usually get it to where you want it to go. For example, double-clicking a Caster will automatically put it in your "Caster Zone" *(the bottom row of the play area)*, and double-clicking a Servant card will put it in the stack area *(chase area)*. Double-clicking that Servant again in the stack will put it into your field.
3. To corrupt an orb, **always use the "peek at card face" command on that card before moving it to your hand!** If you don't, you won't know whether that card has a [Break] ability or not until it's already in a private zone. Every facedown card is numbered, so make sure you keep track of both your and your opponent's facedown cards.
4. As of right now there isn't a way to turn your cards upside-down to represent the "reverse" position. The easiest fix I can offer is to place a counter (preferably red) on the card to mark it as reversed.
5. To use Soulbond Servants, add them to your sideboard (doubleclick from the main deck area, or Ctrl+Enter while the card name is highlighted in the deck editor). To grab them in-game, use Shift+F3 to access your sideboard. When playing a Soul Bond Servant, to mark both of the casters used to summon it to its stock, rightclick those casters and use the Attach to Card command on the Soul Bond servant. To unattach them, rightclick them again.
6. If you can't figure out how to manipulate the cards to do what you want them to do, explore the rightclick menu on all sorts of objects in the window. It has tons of useful options for interacting with the GUI if you can't remember the keyboard shortcuts.
7. When you reveal a servant with [Break], it won't have its ATK/DEF displayed on the bottom right. To fix this, drag it to the stack/chase area, then back into the field.
8. To create a copy of the coin you receive for going second, simply enter the token creation menu (`Ctrl`+`T`) and type "the coin" in the name box. The coin token will appear and the image will download automatically, and to remove it simply drag it to a zone that isn't the field.

## List of Included Sets
* SD01/SD02 Starter Deck [Wings of Anger], [Arrogant Swallowtail] (10/20/17)
* BP01 Booster Pack Vol. 1 [The Magic Battle Begins] (10/20/17)
* BP02 Booster Pack Vol. 2 [πth Dimension Battle Royale] (2/9/18)
* Promo Cards as of 2/9/18

Sets will be added as they're added to the main website. If you'd like to translate Japanese-only sets, let me know and I'll work with you on getting them implemented.

#### Disclaimer
I do not own The Caster Chronicles or contribute to Cockatrice. This is only a text document containing publicly available information. I do not gain anything from this project other than the personal satisfaction that I was able to help spread an awesome game.
