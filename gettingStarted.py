def welcome_assignment_answers(question):
    answers = {
        "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?": "pcap",
        "Are encoding and encryption the same? - Yes/No": "No",
        "Is it possible to decrypt a message without a key? - Yes/No": "No",
        "Is it possible to decode a message without a key? - Yes/No": "Yes",
        "Is a hashed message supposed to be un-hashed? - Yes/No": "No",
        "What is the SHA256 hashing value of your NYU email and use the answer in your code - ": "b92d7fde9b860d26b779dd51c91e0803be956a5b29f5bc33341c909fec15b9fc",
        "Is MD5 a secured hashing algorithm? - Yes/No": "No",
        "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number": "4",
        "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number": "3",
    }

    return answers.get(question, "Question not recognized.")

























