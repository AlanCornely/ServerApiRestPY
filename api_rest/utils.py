import random
from lead_service import LeadService
from database import db

# Função para gerar leads fictícios
def generate_leads():
    
    names = ['John Doe', 'Jane Smith', 'Chris Johnson', 'Patricia Brown', 'Michael Williams']
    interests = ['Tecnologia', 'Saúde', 'Educação', 'Marketing', 'Design']
    telefones = ['(99)99999-9999', '(88)88888-8888', '(77)77777-7777']
    emails = ['aaaaaa@gmmail.com', 'bbbbbbbbbb@gmail.com', 'ccccccccccc@gmail.com']

    # Cria uma instância de LeadService com o db
    lead_service = LeadService(db)

    for _ in range(100):
        name = random.choice(names)
        latitude = random.uniform(-90, 90)
        longitude = random.uniform(-180, 180)
        temperature = random.uniform(1, 10)
        interest = random.choice(interests)
        email = random.choice(emails)
        telefone = random.choice(telefones)
        
        # Usa a instância de LeadService para criar o lead
        lead_service.create_lead(name, latitude, longitude, temperature, interest, email, telefone)
        
