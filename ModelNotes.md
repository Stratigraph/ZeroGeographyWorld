Zero-Geography Model
============================================

Basic Mechanics
---------------------------------------------

There are initially N interests and N agents, one interest per agent.

### Each tick: 

Two interests become active at random. This is an attempt to
capture 'proximate activation' (Cederman) / the coupling of opportunity and risk. 

Assuming the two Interests belong to different agents:

Agents place bids / allocate resources to both interests, as follows:

- Resources to own interest = Total Wealth * ( Interest Value) / (All Interests)

- Resources to other interest = Total Wealth * (Interest Value) / (All Intersts + Interest Value)

If both Interests belong to the same agent:

- The lower-valued Interest is spun off into an independent actor, with starting
wealth = (interest val) / (total interest vals) * total wealth

This captures several intuitions:
- Agents value the interests they have more than potential interests (loss aversion); they allocate defensive resources first, and will value identical interests higher if they posess them than if the other does.

- Strong agents have an inherent advantage over weak ones.

- Weaker agents may be able to fend off stronger agents if the interest at risk is a 'core interest' (e.g. a large fraction of their total), while only represents a small gain for the strong agent.

Whichever agent places the higher 'bid' on an interest takes control of it.








