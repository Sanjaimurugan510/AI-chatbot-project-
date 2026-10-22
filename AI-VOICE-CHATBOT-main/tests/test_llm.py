from services.chatbot import get_ai_response


question = "Explain RAG in simple English."


answer = get_ai_response(question)


print("\nUser:")
print(question)


print("\nGemini:")
print(answer)