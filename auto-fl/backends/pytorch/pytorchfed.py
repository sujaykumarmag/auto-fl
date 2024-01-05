class PytorchFederated():
    def __init__(self,clients):
        print("Federated Learning for Pytorch")
        self.clients = clients
    
    def create_dataset(self):
        print(f"dataset size / {self.clients}")
        