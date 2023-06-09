from email.mime.text import MIMEText
from email.utils import formataddr
import smtplib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import numpy as np

def retry_decorator(retries=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(retries):
                try:
                    func(*args, **kwargs)
                    break
                except Exception as e:
                    print(f"Failed to send notification. Error: {e}")
                    if i < retries - 1:  # If not the last retry
                        print("Retrying...")
                    else:  # On last retry, raise error
                        raise
        return wrapper
    return decorator


class NotificationCallback():
    def __init__(self, sender_email, sender_auth, receiver_email, server="smtp.qq.com", port=465):
        self.sender_email = sender_email
        self.sender_auth = sender_auth
        self.receiver_email = receiver_email
        self.server = server
        self.port = port
        self.epoch = 0

    def on_train_begin(self):
        self.epoch = 0

    def on_epoch_end(self, metrics):
        val_loss, accuracy = metrics[0], metrics[1]
        message = f"epoch: {self.epoch} val loss: {val_loss:.7f} val acc: {accuracy:.7f}"
        # self.send_notification(message)
        print(message)
        self.epoch += 1
        
    def on_train_end(self, metrics):
        val_loss, accuracy = metrics[0], metrics[1]
        message = f"epoch: {self.epoch} val loss: {val_loss:.7f} val acc: {accuracy:.7f}"
        self.send_notification(message)
    
    @retry_decorator()
    def send_notification(self, msg, subject="Training Update", from_email="ML Training", to_email="User"):
        msg = MIMEText(msg, 'plain', 'utf-8')
        msg['From'] = formataddr([ from_email, self.sender_email])
        msg['To'] = formataddr([to_email, self.receiver_email])
        msg['Subject'] = subject

        server = smtplib.SMTP_SSL(self.server, self.port)
        server.login(self.sender_email, self.sender_auth)
        server.sendmail(self.sender_email, [self.receiver_email, ], msg.as_string())
        server.quit()


class ModelTraining:
    def __init__(self):
        self.callbacks = []

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def on_train_begin(self):
        for callback in self.callbacks:
            callback.on_train_begin()

    def on_epoch_end(self, metrics):
        for callback in self.callbacks:
            callback.on_epoch_end(metrics)
            
    def on_train_end(self, metrics):
        for callback in self.callbacks:
            callback.on_train_end(metrics)

    def train_model(self):
        # loading some example data
        iris = load_iris()
        X = iris.data
        y = iris.target

        # split the data with 50% in each set
        X1, X2, y1, y2 = train_test_split(X, y, random_state=42, train_size=0.5, stratify=y)

        # fit the model on one set of data
        model = LogisticRegression(max_iter=200)

        self.on_train_begin()

        for i in range(100): # assuming 100 epochs
            model.fit(X1, y1)

            # evaluate the model on the second set of data
            score = model.score(X2, y2)

            # simulate loss
            loss = np.random.rand()

            # notify on epoch end
            self.on_epoch_end((loss, score))
        
        # notify on train end
        self.on_train_end((loss, score))


if __name__ == '__main__':
    sender_email = "sender@email.com" 
    sender_auth = "sender_auth"
    receiver_email = "receiver@email.com"
    training = ModelTraining()
    training.add_callback(NotificationCallback(sender_email, sender_auth, receiver_email))
    training.train_model()
