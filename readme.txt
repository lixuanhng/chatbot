This practice focuses on a simple retrieval chatbot demo.

In the beginning of practice, we put QA pair into BERT to train text similarity model. After loading the short dialogue into the system, user will be asked to input A Question from keyboard. The system will only return one in similar to the Question, waiting for confirmation from user. If user answer 'Yes', the right answer will be returned and process terminates; otherwise, a new similar question will be returned. If user refuses 3 returned questions contiinuously, the system will suggest user to call service support for help.

Go run read_qa.py to check the experiment results.

I guess this practice is quite esay actually. More experiments will put into Dialogue Management.

If you get questions or interest in it, you are more than welcome to contact and join me. Thanks very much.