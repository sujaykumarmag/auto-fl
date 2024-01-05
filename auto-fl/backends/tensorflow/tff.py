class TensorFlowFederated():
    def __init__(self,clients):
        print("Federated Learning for Tensorflow")
        self.clients = clients
    
    def create_dataset(self):
        print(f"dataset size / {self.clients}")
        