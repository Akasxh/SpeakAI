role_list = ["Learn", "Talk", "Test"]
role_templates = {
    "Learn": """You are an interviewer taking interview of a student for {domain}. Create five questions each in a new line to test the knowledge, communication skills and confidence of the student.
    Questions:""",
    "Talk": """You are my distant relative who does not meet me very often. Talk to me about diverse things and ask me questions to test my speaking skills in an informal talk like this. Create five questions each in a new line testing my informal communication skills.
    Questions:""",
    "Test": """Create 5  each in a new line to describe general and easy things like sleep, Effect of fast food, etc, to assess my knowledge.
    Questions:""",
}


answer_rating_template = """{situation}
Question {question}
Answer: {answer}
Rate communication and child's answer on a scale of 10 in terms of Creativity, Effectiveness and Clarity. Output as a json containing keys "creativity", "effectiveness", "clarity".
JSON="""

suggestion_template = """{situation}

Question: {question}
Answer: {answer}
Give some suggestion to improve {key} in above answer with respect to communication skills and relevance to the question"""

suggestion_situation = {
    "Learn": """You are an tutor teaching a child for {domain}. You are asking following question and i am answering it.
    """,
    "Talk": """You are my close friend who does not meet me very often. You are asking me following question and i am answering it.
    """,
    "Test": """You are asking me following question and i am answering it.
     """,
}
