# Senmal
Simple Email Notification of Machine Learning

## Description

The `senmal` project comprises a function, `send_notification`, which is designed to send email notifications. While this function can be utilized in various applications, an illustrative use-case is provided in `example.py`, demonstrating its utility in the context of tracking the training progress of machine learning models.

This project contains two Python scripts:

1. `send_notifications.py`: Defines the `send_notification` function which takes various parameters such as sender's email, receiver's email, message to be sent, etc. This function can be employed to send notifications in various scenarios.

2. `example.py`: An example application of the `send_notification` function in a machine learning training scenario. It trains a logistic regression model on the Iris dataset, and after each epoch, an email notification about the loss and accuracy of the model on the validation set is sent.

## Dependencies

The main function, `send_notification`, requires the following Python libraries:

- smtplib
- email

For the example application (`example.py`), the following additional libraries are necessary:

- sklearn
- numpy

## Usage

To use the `send_notification` function:

1. Import the function into your Python script from `send_notifications.py`.

2. Configure the function parameters according to your requirements (sender's email, receiver's email, message, etc.)

For the example application:

1. Update the `sender_email` and `sender_auth` with the sender's email ID and the sender's authentication key in `example.py`.

2. Update the `receiver_email` with the receiver's email ID in `example.py`.

3. Run `example.py` to start training the model. After each epoch, an email will be sent with the loss and accuracy of the model on the validation set.

```bash
python example.py
```

## Note

This project uses the SMTP server provided by QQ, you may need to replace it with your preferred email server. The port used is 465, which is common for SMTP servers. If your server uses a different port, you should update it in the scripts.

Also, remember to enable access for less secure apps in your email account settings if you're using Gmail or similar providers.