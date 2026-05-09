from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import json

app = FastAPI()

# Load catalog
with open('shl_catalog.json', 'r') as f:
    assessments = json.load(f)

print(f"✅ Loaded {len(assessments)} assessments")

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

class ChatResponse(BaseModel):
    reply: str
    recommendations: List[dict]
    end_of_conversation: bool

def search_assessments(query, k=5):
    query = query.lower()
    scored = []
    
    for a in assessments:
        score = 0
        text = (a['name'] + ' ' + a['skills'] + ' ' + a['description']).lower()
        
        words = query.split()
        for word in words:
            if len(word) > 2 and word in text:
                score += 1
        
        if score > 0:
            scored.append((score, a))
    
    scored.sort(reverse=True, key=lambda x: x[0])
    return [a for score, a in scored[:k]]

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    user_msgs = [m for m in request.messages if m.role == "user"]
    if not user_msgs:
        return ChatResponse(
            reply="Hello! I can help find SHL assessments. What role are you hiring for?",
            recommendations=[],
            end_of_conversation=False
        )
    
    query = user_msgs[-1].content
    
    off_topics = ['weather', 'stock', 'legal', 'resume', 'salary', 'interview tips']
    if any(word in query.lower() for word in off_topics):
        return ChatResponse(
            reply="I can only recommend SHL assessments. Please tell me about the role you're hiring for.",
            recommendations=[],
            end_of_conversation=False
        )
    
    if len(query) < 8 or query.lower() in ['hi', 'hello', 'help', 'hey']:
        return ChatResponse(
            reply="Please tell me more about the role. For example: 'I need to hire a Java developer'",
            recommendations=[],
            end_of_conversation=False
        )
    
    results = search_assessments(query, k=5)
    
    if not results:
        return ChatResponse(
            reply="I couldn't find matching assessments. Could you describe the role or required skills?",
            recommendations=[],
            end_of_conversation=False
        )
    
    recommendations = [
        {
            "name": r['name'],
            "url": r['url'],
            "test_type": r['test_type']
        }
        for r in results[:5]
    ]
    
    reply = f"Here are {len(recommendations)} assessments for '{query}':"
    
    return ChatResponse(
        reply=reply,
        recommendations=recommendations,
        end_of_conversation=True
    )
