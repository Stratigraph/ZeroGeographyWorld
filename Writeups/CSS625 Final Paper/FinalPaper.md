---
title: 'Toward a Zero-Geography Model of Geopolitics'
author:
- name: David Masad
  affiliation: George Mason University

abstract: |
	This is the abstract.

bibliography: ZGPaper.bib
...

# Introduction

# Method of Analysis

## Model assumptions

I introduce an initial implementation of a geography-free model of an
international system. The model attempts to capture the following assumptions:

1. The world is composed of political actors, endowed with resources and competing with each other for the means to acquire additional resources.

2. Actors' interactions with one another are driven by specific interests, which become salient exogenously.

3. All actors have loss aversion, and will prioritize defending their current interests over expanding their influence.

4. Strong actors will tend to act more frequently than weak actors, and interact with a wider range of actors.

4. Strong actors will generally have an advantage over weak ones.

5. Weak actors may nevertheless be able to defeat stronger actors over issues that are much more salient to the weak actor than the stronger one.

6. Weak actors with no ability to gain additional resources cease to be relevant actors.

These assumptions are generally similar to the driving assumptions of the geopolitical models described above, particularly GeoSim. Like GeoSim, the model as implemented here does not include alliances. As argued by [@min_2008], alliances represent an important component of an international system, and one which is likely to influence the outcomes significantly; as such, a detailed aspatial alliance model is outside the scope of this paper. However, as [@cederman_1997] demonstrates, many features of an international system may emerge even in the absence of alliances. Furthermore, I will argue that some features of alliances emerge endogenously from the model's logic.

## Model description

Formally, the model is composed of two types of entitites: **Actors** and **Interests**. Interests are activated (become salient) at random, allowing their owners to expend resources to protect their own interests and attempt to dominate the other's. Finally, actors gain resources based on the interests they currently control.

### Interests and Actors

Interests take the role that provinces play in GeoSim and AWorld; they are the atomic entities from which actors are assembled. Like provinces, each interest is owned by exactly one actor at any given time. Whereas provinces represent discrete geographic entities, interests are meant to be more abstract: they may represent a piece of geography, but also access to a natural resource, an international institution, or even a source of 'soft power' or social capital; in short, any source of power in an international system. 

Actors represent primarily states, though they may be any autonomous actor in an international system, including non-governmental advocacy organizations, transnational militants, and more. Actors must posess at least one interest in order to be active. They are endowed with an abstract measure of power and influence (which I will call *wealth*) based on the interests they control, and which they expend in defense of their current interests and in order to acquire additional interests.

### Model Tick

The model proceeds in **ticks**, with each tick representing an interaction between (generally) two actors. A tick proceeds as follows:

1. Two interests are chosen uniformly at random to become active.
2. The actors who control these interests are activated. Assuming the interests are owned by different actors:
3. Both actors simultaneously allocate wealth toward both active interests, as described below. This wealth is subtracted from the actors' endowment of wealth.
4. The actor who allocated the most wealth to each interest gains or maintains control of it. 

After one interaction concludes, two more interests are activated at random, beginning the next interaction. Additionally, after every set number of interactions, all actors gain resources based on the total value of interests they currently control.

Note that there is no reason to assume that interactions represent evenly-spaced time-steps; rather, they represent opportunites for change in the world. Thus, unrelated interactions (i.e. ones with no overlapping interests or actors) may even be taking place simultaneously, while other interactions may represent events occuring days or months apart.

### Actor Decisionmaking




# Results and Findings

# Discussion

# Summary
