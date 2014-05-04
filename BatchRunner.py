import json
from Model import Model

class BatchRunner(object):

    def __init__(self, initialization, iter_count, step_count, **kwargs):
        '''
        Set up a batch of models to run.
        '''

        self.models = []
        self.model_outputs = []
        self.step_count = step_count

        # Prepare models
        for i in range(iter_count):
            m = Model()
            # Set the parameters:
            for attr, val in kwargs.items():
                if hasattr(m, attr):
                    setattr(m, attr, val)
            self.models.append(m)

        # Run model prep:
        for model in self.models:
            if initialization == "base_model":
                model.base_model()
            elif initialization == "burnin_model":
                if "num_agents" in kwargs:
                    model.burnin_model(kwargs["num_agents"])
                else:
                    raise Exception("num_agents argument needed for burn-in.")
            elif initialization == "set_polarity":
                if "large_agents" in kwargs and "fraction_large" in kwargs:
                    model.set_polarity(kwargs["large_agents"], kwargs["fraction_large"])
                else:
                    raise Exception("large_agents and fraction_large arguments needed")

    def run_all(self, verbose=False):
        for i, model in enumerate(self.models):
            if verbose:
                print "Running", i
            model.run_model(self.step_count)
            self.model_outputs.append(model.to_dict())

    def export_results(self, filepath):
        '''
        Write the model_outputs to a JSON file.
        '''
        f = open(filepath, "wb")
        json.dump(self.model_outputs, f)
        f.close()
        


