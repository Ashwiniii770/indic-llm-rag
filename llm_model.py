def generate_answer(context, question):
    
    answer = f"""
Question: {question}

Answer:
{context}
"""
    
    return answer