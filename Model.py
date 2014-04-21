'''
Zero-Geography Model
======================================

A model of interest-oriented agent interaction.
'Interests' are abstract generalizations of the provinces in GeoSim, AWorld 
and elsewhere. 

'''
from __future__ import division
import random


class Interest(object):
    '''
    The atomic element of the model.
    '''

    def __init__(self, id_num, owner, value):
        '''
        Create a new Interest

        Args:
            id_num: A unique identifier
            owner: An Agent object 
            value: The Interest's value / contibution to the owner
        '''
        self.id_num = id_num
        self.owner = owner 
        self.value = value

class Agent(object):
    '''
    Agents represent states, and must have one or more Interests associated
    with them.
    '''

    def __init__(self, id_num, model):
        '''
        Create a new Agent.

        Args:
            id_num: A unique identifier
            model: A model object the Agent is associated with
        '''
        self.id_num = id_num
        self.wealth = 0
        self.model = model
        self.interests = [] # List of owned interests

    def add_interest(self, interest):
        '''
        Associate an Interest with this agent.
        '''
        interest.owner = self
        self.interests.append(interest)

    def grow_resources(self):
        '''
        Increment resources at the end of each turn.
        '''
        for interest in self.interests:
            self.wealth += interest.value

    def total_values(self):
        return sum([interest.value for interest in self.interests])

    def allocate_resources(self, interest):
        '''
        Allocate resources pointed at a given Interest, not necessarily owned.
        '''

        if interest in self.interests:
            total = self.total_values()
        else:
            total = self.total_values() + interest.value
        
        proportion = interest.value / total
        allocation = self.wealth * proportion
        self.wealth -= allocation

        return allocation


class Model(object):
    '''
    The actual model management class.
    '''

    def __init__(self):
        '''
        Create a new model.
        '''
        self.interest_count = 100
        self.interests = []
        self.agents = []
        self.verbose = False
        self.bid_sizes = []
        #self.setup_model()


    def setup_model(self):
        '''
        Initialize the model with one interest per agent.
        '''

        # Create the interests and agents together, one agent per interest.
        for i in range(self.interest_count):
            agent = Agent(i, self)
            value = random.randint(1, 100)
            interest = Interest(i, agent, value)
            agent.add_interest(interest)
            self.interests.append(interest)
            self.agents.append(agent)

    def burnin_model(self, num_agents):
        '''
        Initialize the model such that the interests are randomly distributed
        among some number of agents.
        '''
        # Initialize agents
        for i in range(num_agents):
            agent = Agent(i, self)
            self.agents.append(agent)

        # Distribute interests:
        for i in range(self.interest_count):
            value = random.randint(1, 100)
            agent = random.choice(self.agents)
            interest = Interest(i, agent, value)
            self.interests.append(interest)
            agent.add_interest(interest)


    def interaction(self):
        '''
        Run a single interaction.
        An interaction goes as follows:
            Two Interests become active.
            Their owners place bids on each, in proportion to their valuation.
            The agent with the higher bid on each takes control of the Interest
        '''
        # Choose interests
        interest0 = random.choice(self.interests)
        interest1 = random.choice(self.interests)
        while interest1 is interest0:
            interest1 = random.choice(self.interests)

        # Activate their owners
        owner0 = interest0.owner
        owner1 = interest1.owner

        # If both interests belong to the same actor, jettison the lowest
        # one with a proportion of its wealth.
        if owner0 is owner1:
            min_interest = min([interest0, interest1], 
                key=lambda x: x.value)

            new_owner = Agent(random.randint(100, 999), self)
            wealth = owner0.allocate_resources(min_interest)
            self.transfer_interest(min_interest, new_owner)
            new_owner.wealth = wealth
            #new_owner.wealth = min_interest.value
            self.agents.append(new_owner)
            return

        # Print-debug
        if self.verbose:
            print "Active interest", interest0.id_num, "(", interest0.value, ")"
            print "Active interest", interest1.id_num, "(", interest1.value, ")"

        # Get their bids:
        
        # Agent 0's bids:
        bid_00 = owner0.allocate_resources(interest0)
        bid_01 = owner0.allocate_resources(interest1)

        # Agent 1's bids:
        bid_11 = owner1.allocate_resources(interest1)
        bid_10 = owner1.allocate_resources(interest0)

        # Evaluate ownership:
        if bid_01 > bid_11:
            self.transfer_interest(interest1, owner0)
        if bid_10 > bid_00:
            self.transfer_interest(interest0, owner1)

        self.bid_sizes += [bid_00, bid_01, bid_11, bid_10]


    def transfer_interest(self, interest, new_owner):
        '''
        Transfer an interest from its old owner to the new one.
        '''
        old_owner = interest.owner
        old_owner.interests.remove(interest)
        new_owner.add_interest(interest)

        if self.verbose:
            print "Transfering", interest.id_num, "from", old_owner.id_num, "to", new_owner.id_num















