# Senmal
Simple Email Notification of Machine Learning

## Description

The `senmal` project is a simple system designed to train a machine learning model and send email notifications about the training progress and results. This project is mainly useful for remote training tasks where direct monitoring might not be possible. By receiving these notifications, you can keep track of how well your model is training.

The project contains two main Python scripts:

1. `send_notifications.py`: This script is used to send email notifications about the training status of the model. It defines the `send_notification` function which takes various parameters such as sender's email, receiver's email, message to be sent, etc.

2. `example.py`: This script is used for model training. It trains a logistic regression model on the Iris dataset. After each epoch, it sends an email notification about the loss and accuracy of the model on the validation set.

## Dependencies

The project requires the following Python libraries:

- smtplib
- email
- sklearn
- numpy

## Usage

To use this project:

1. Update the `sender_email` and `sender_auth` with the sender's email ID and the sender's authentication key in both `example.py` and `send_notifications.py`.

2. Update the `receiver_email` with the receiver's email ID in both `example.py` and `send_notifications.py`.

3. Run `example.py` to start training the model. After each epoch, an email will be sent with the loss and accuracy of the model on the validation set.

```bash
python example.py
```

## Note

This project uses the SMTP server provided by QQ, you may need to replace it with your preferred email server. The port used is 465, which is common for SMTP servers. If your server uses a different port, you should update it in the scripts.

Also, remember to enable access for less secure apps in your email account settings if you're using Gmail or similar providers.