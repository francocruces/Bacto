# Franco Cruces' Bacto
Bacto is a real time strategy game implemented in python.

## How to play

### Unit
Units are the most atomic level of the game logic. They have an owner and can battle against enemy units.

### Base / Colony
It is a fixed location on the game surface that can store units. Every base either has a player as the owner or is a neutral base. Every base will generate units through time for the current owner. 

### Race
Each player can choose a race at the beggining of a match. Each race has a particular set of values for, production time, speed, attack and defense.

### Mechanics
At any moment, a player is able to start units to move from a base he owns to another base; if the target's owner and the moving player are the same, the units will simply add up to the units that are already stored at the base; otherwise, a battle starts, and the winner becomes the owner of the target.

### Objective
A player is declared winner once there aren't any colonies or moving parties owned by an enemy player.

## Current development status
Bacto currently supports Random matches with a given amount of neutral colonies, and Custom matches with preset maps.

New maps and Races can be easily added following instructions provided in either /data/maps or /data/races.

## The future of Bacto
An story mode would be the next big step for bacto, with RPG elements and boss battles.

A more intelligent enemy AI isn't easy to implement, as it would need to consider every race attribute and plan in a smart way.

## How to run
Requires pygame and numpy to run. Simply run main.py.

## Music
Original soundtrack composed and played by Franco Cruces Ayala.

Soundcloud: https://soundcloud.com/franco-cruces

YouTube: https://www.youtube.com/channel/UCgK_EnmLzWa9v8pANQfXsrg
