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

5. Strong actors will generally have an advantage over weak ones.

6. Weak actors may nevertheless be able to defeat stronger actors over issues that are much more salient to the weak actor than the stronger one.

7. Weak actors with no ability to gain additional resources cease to be relevant actors.

These assumptions are generally similar to the driving assumptions of the geopolitical models described above, particularly GeoSim. Like GeoSim, the model as implemented here does not include alliances. As argued by [@min_2008], alliances represent an important component of an international system, and one which is likely to influence the outcomes significantly; as such, a detailed aspatial alliance model is outside the scope of this paper. However, as [@cederman_1997] demonstrates, many features of an international system may emerge even in the absence of alliances. Furthermore, I will argue that some features of alliances emerge endogenously from the model's logic.

## Model description

Formally, the model is composed of two types of entitites: **Actors** and **Interests**. Interests are activated (become salient) at random, allowing their owners to expend resources to protect their own interests and attempt to dominate the other's. Finally, actors gain resources based on the interests they currently control.

### Interests and Actors

Interests take the role that provinces play in GeoSim and AWorld; they are the atomic entities from which actors are assembled. Like provinces, each interest is owned by exactly one actor at any given time. Whereas provinces represent discrete geographic entities, interests are meant to be more abstract: they may represent a piece of geography, but also access to a natural resource, an international institution, or even a source of 'soft power' or social capital; in short, any source of power in an international system. 

Actors represent primarily states, though they may be any autonomous actor in an international system, including non-governmental advocacy organizations, transnational militants, and more. Actors must posess at least one interest in order to be active. They are endowed with an abstract measure of power and influence (which I will call *wealth*) based on the interests they control, and which they expend in defense of their current interests and in order to acquire additional interests.

### Model Tick

The model proceeds in **ticks**, with each tick representing an interaction between (generally) two actors. A tick proceeds as follows:

1. Two interests are chosen uniformly at random to become active.
2. The actors who control these interests are activated. 
    1. If both actors have only one interest, they merge together, combining both interests and wealths.
	2. If at least one actor has two or more interests, both actors simultaneously allocate wealth toward both active interests based on the decision rule described below. This wealth is subtracted from the actors' endowment of wealth. The actor who allocated the most wealth to each interest gains or maintains control of it. 
	3. If both interests are owned by the same actor, this represents *internal conflict*, which is described below.

After one interaction concludes, two more interests are activated at random, beginning the next interaction. Additionally, after every set number of interactions, all actors gain resources based on the total value of interests they currently control.

Note that there is no reason to assume that interactions represent evenly-spaced time-steps; rather, they represent opportunites for change in the world. Thus, unrelated interactions (i.e. ones with no overlapping interests or actors) may even be taking place simultaneously, while other interactions may represent events occuring days or months apart.

### Actor Decisionmaking

Most interactions involve interests owned by two different actors. From the perspective of each actor, they are defending the interest they own and attacking the other's interest. The actors allocate wealth to each in proportion to its fraction of their total wealth. 

Formally, let $i$ and $j$ designate the actors, with $w_i$ and $w_j$ their respective wealths. Actor $i$ has $n$ interests, with their values designated $v_0$ through $v_m$. Let $v_*$ be the interest $i$ is defending, and $v_j$ the interest owned by $j$ which $i$ is attacking. The wealth $w(v)$ allocated to each interest is:

$w(v_*)=w_i\frac{v_*}{\sum_{k=0}^{m}v_k}$

$w(v_j)=(w_i - w(v_*))\frac{v_j
}{\sum_{k=0}^{m}v_k + v_j}$

This decision rule corresponds to assumptions 3-6, as described above. The more wealth an actor has, the more, in absolute terms, they will be able to allocate to both active interests. However, a to high-wealth actor, a given interest may represent only a small fraction of their total interests, and thus they may allocate fewer resources toward it. An actor with a single interest, in contrast, will always devote *all* its wealth to defending it. Note also that given two interests of identical value, the rules above ensure that actors will allocate more resources to defending the interest they own over an identically-valued interest they are attacking.

### Internal Conflict

As actors accumulate more interests, the chances increase that two interests will become activated which both belong to the same actor. This captures the issue of internal conflict: as political actors grow and expand to include more diverse interests, the chances that these interests will come into conflict increases. 

I experiment with two different mechanisms for resolving internal conflicts:
* **Internal resolution** simply requires the owner to expend wealth to defend both interests, following the rule described above. This represents the actor expending resources to resolve the conflict and maintain the status quo.
*  **External resolution** assumes that the conflict may only be resolved by jettisoning one of the conflicting interests. Under this rule, the lower-valued interest is removed from the actor, becoming an independent actor with initial wealth equal to what the original owner would have expended defending it. 

These are highly simplified rules, which only correspond to some ways such conflicts are resolved in reality. However, they are sufficiently different as to facilitate experiments capturing the difference between the resolution rules.

## Model Setup

I run four experiments, varying the internal conflict mechanisms and the initial conditions. The first model initialization involves 100 interests, each initially associated with a single agent. This represents a 'cold start' where aggregate actors have not yet formed. The second initialization can be thought of as burned-in, with higher resolution: it involves 1,000 interest, distributed randomly among 100 actors. This represents a 'more complex' system (in the social-complexity sense), where actors are already aggregations of interests, with each specific interest having reduced bearing on the system as a whole.

Each combination of internal conflict mechanism and initialialization constitutes an experiment, for 4 experiments total. Each experiment involves 100 random model instantiations. The cold-start models are run for 1,000 steps, while the burn-in models are run for 10,000 steps. Across all models, interests are created with a random value selected from a uniform random distributions of the integers between 1 and 100.

## Analysis

For each experiment, I will present a representative run, including the initial and final distributions of interests among agents, and the change in the number of active agents over time. 

At each step of each run, I will compute the Gini coefficient of the distribution of interests across all active agents. This will provide a normalized way of assessing how concentrated or dispursed ownership of interests (and hence power) is within the system. By plotting the Gini coefficents of all runs in each experiment together, I will visualize overall patterns that each system converges to, as well as any deviations from them.

Finally, I will fit a power law distribution to each timestep of each model run. Note that initially, when the distribution of interests is approximately uniform, a power law will be a poor fit -- it will not in fact describe the distribution. Nevertheless, by plotting the best-fit power law coefficient at each step, we will be able to identify the phase shift occuring when the system converges to a heavy-tailed distribution.


# Results and Findings

## Experiment 1

The models under this experiment exhibit convergence toward strong consolidation into a single actor. Figure X shows a representative run of the model. Initially, the number of actors plummets rapidly as singletons consolidate together. Past an inflection point, all or most of the actors are likely aggregate, multi-interest entities, and the consolidation slows, yet continues. Even the period of bipolarity, with two actors, does not last long, and the model converges to a single actor.

This pattern is robust across all runs of this experiment. Figure X shows the Gini coefficient from all model runs plotted together, and demonstrates that they all exhibit a very similar dynamic. All runs exhibit rapid initial consolidation; while there is some variation in the pace at which the number of aggregate actors narrows, by shortly after step 200, all model runs have consolidated into a single actor, as indicated by the Gini coefficient of 1. 

Figure X shows the fitted $\alpha$ parameter across each run. During the period of consolidation, a power law is often a poor fit, and the fitted parameter takes on a wide range of values we would not expect to observe in a real power law. Nevertheless, as the model converges toward a small number of actors, the weight of the distribution of $\alpha$s begins to accumulate on plausible values slightly below 2. This strongly suggests that at this point, even the apparently multipolarity suggested by the counts of interests per actor is misleading: there is already likely to be one actor with the bulk of interests, while the actors who remain are substantially smaller, and hence weaker. Here, the appearance of the plausible scale-free distribution helps indicate when the system begins to become unipolar. Note the maximum value of the x-axis in Figure X; once there is only one actor remaining, there cannot be a distribution of interests, and thus no distribution parameter.

## Experiment 2

This experiment uses the external resolution rule described above, and hence features a new potential phenomenon not exhibited in the previous experiment: the appearance of new actors. This is demonstrated by the representative run in Figure X: initially, the model behaves very much as in the previous experiment, with a rapid consolidation of interests. However, at a certain point, a new process takes over, and the number of actors begins to percolate, showing cyclic-seeming behavior but overall remaining stably-higher than the previous minima. Note the distribution of interests, shown in Figure X. While the end state exhibits many actors, all but one control no more than 5 interests, with most only controlling one or two; there is a single actor dominating the system and dominating nearly half the interests within it.

The Gini coefficients across runs confirm this. While the curve appears shallower than in the previous experiment (and never reaches 1), it shows a very similar trajectory, with a period of rapid consolidation followed by a slower convergence toward a single unitary actor. Note that the fluctuations which characterize the actor count are completely absent from the Gini charts. There is still a dominant actor while new actors appear due to internal conflict, and some may survive and even combine with other cast-off interests, none grow large enough to change the balance of power.

Like the previous experiment, the power law fit is initially weak, as shown in Figure X. However, to a greater extent than in the previous experiment, this model appears to exhibit a strong phase shift, converging to a coefficient close to 2, though making regular, frequent jumps above it, though always staying below 3. This appears to be the state where there is one dominant actor, surrounding by a 'foam' of actors cast off of the dominant actor due to internal conflict, consolidating with others, and ultimately reabsorbed by the dominant actor.

## Experiment 3

We may naively expect this experiment to have similar dynamics to those observed in Experiment 1, and indeed they are similar in one key respect -- the internal resolution rule means that the number of actors may only go down. Nevertheless, the trajectory by which the number of actors declines is clearly different, as the representative run in Figure X shows. While the model still converges to a single all-encompassing actor, the rate of convergence appears to be strictly linear. 

The Gini coefficients plotted in Figure X show similar dynamics. While they are not quite as linear as Figure X, they nevertheless do not exhibit the inflection point in both previous Gini plots. 

Similarly, the power law coefficient in Figure X does not exhibit a phase shift. In fact, unlike in the previous experiments, the bulk of the distribution is not on a plausible power-law coefficient, though there is a general trend toward convergence.

## Experiment 4

The results of this experiment show perhaps the most striking results. The representative run showed in Figure X shows not just one phase shift but 2. There is an initial relatively steady increase in the number of actors, until approximately step 1,500, when the rate at which new actors appears suddenly spikes, rapidly increasing until shortly after step 2,000, when the number of agents stabilizes, beginning to randomly oscillate around 400 actors, a state which persists throughout the rest of the model run.

The Gini coefficient plot (Figure X) shows a similar kink, unseen in any of the previous Gini plots. Robustly, across multiple runs, the Gini coefficient rises, then dips, bottoms out, and increases again, slowly approaching 1 though never fully converging.

The power law coefficient plot shows a similar kink; the wide, downward-sloping initial behavior resembles Experiment 3; it is followed by a dramatic, near-discontinuous jump, and an stable equilibrium slightly above 3, a plausible though extreme power law coefficient. 

# Discussion

We can analyze the behavior of this model along two lines. While the previous section discusses the results in a self-contained manner, we must remember that our original intent was to simulate an international system; thus, the model results ought to be able to tell us something about international relations. Additionally, the model presents and illustrates several broader issues in the behavior of complex systems, and the challenges involved in modeling and analyzing them.

There is one key force which exhibits itself across all the model runs presented above, regardless of the experiment: a strong tendency towards unipolarity. All the model runs begin with a relatively equitable distribution of interests -- and hence of resources and power. Yet by the end of each and every model run, a single actor will have emerged as the sole 'superpower', controlling a disproportionate number of interests. Under the internal conflict resolution rules, no new actors are inserted into the model, leading to only a single actor remaining active. Yet even under the external rule, when new actors appear regularly, the superpower ends up controlling nearly 50% of all interests, while none of the remaining actors control more than a handful each. This suggests that the convergence to unipolarity is not merely a function of the one-way movement of actor counts under the internal rule, but an emergent result of the system as a whole.

Indeed, it is easy to see how this process occurs. Actor resources exhibit positive feedback: as an actor gains control of additional interests, it acquires more resources which make it more likely to gain control of yet more interests. At some point, an actor may cross an event horizon of sorts, by which it has accumulated sufficient wealth to devote more resources to any interest than any other actor can. Similarly, actors with fewer or lower-valued interests will have less wealth to defend them with, making them more likely to lose control of those interests in any interaction.

As noted earlier, interests function similarly to provinces in previous models. Yet those models did not exhibit the strong convergence to unipolarity exhibited here. This helps point us toward a potential role that geography plays, and in particular the limitation of actors to local conflict only. In the geographic models, the set of potential interactions at any given time is limited. This provides multiple actors with a chance to grow strong by conquering their neighbors before coming into conflict with one another -- local unipolarity giving rise to system-wide multipolarity. The geography-free model has no such constraint, allowing relatively powerful actors to come into conflict earlier, as well as competing for the same available resources (in the form of interests held by weaker actors) -- with inevitable negative consequences for the loser.

The international relations literature has also drawn a connection between globalization and unipolarity. [[ INSERT SOME REFERENCES HERE ]].

A property of this model is that more powerful actors are more likely to be activated, which gives them additional opportunities to further increase their power. This property bears resemblence to another one found in many complex systems: preferential attachement. Particularly in network models, preferential attachement is known to drive the formation of scale-free networks, characterized by power-law distributions of degrees. In this case, number of interests only approximately resembles network degree, and indeed it appears that the distribution of interests, while frequently long-tailed, may not follow a strict power law. Nevertheless, it is noteworthy that across domains, qualitatively similar processes yield qualitatively similar results.

While the convergence to unipolarity is robust across all the experiments, many of the model's other dynamics are not. In particular, the convergence process varied qualitatively between different initial conditions, model scales and resolution rules. It is not clear whether one set of initial conditions is more correct than others, particularly with a model like this where there is not a one-to-one mapping between model entities and the real world. It should not be surprising that in a complex system, initial conditions have a substantial effect not only on the outcome but on the dynamics -- yet such variation has not been deeply explored in many previous geopolitical models. 

# Summary
