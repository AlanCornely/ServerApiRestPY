from models import Lead

class LeadService:
    def __init__(self, db):
        self.db = db

    def create_lead(self, name, latitude, longitude, temperature, interest, email, telefone):
        lead = Lead(name=name, latitude=latitude, longitude=longitude, temperature=temperature, interest=interest, email=email, telefone=telefone)
        self.db.session.add(lead)
        self.db.session.commit()

    def get_all_leads(self):
        return Lead.query.all()

    def get_lead_by_id(self, lead_id):
        return Lead.query.get_or_404(lead_id)
    
    def get_paginated_leads(self, page=1, per_page=50):
        return Lead.query.paginate(page=page, per_page=per_page, error_out=False)

    def update_lead(self, lead_id, name, latitude, longitude, temperature, interest, email, telefone):
        lead = self.get_lead_by_id(lead_id)
        lead.name = name
        lead.latitude = latitude
        lead.longitude = longitude
        lead.temperature = temperature
        lead.interest = interest
        lead.email = email
        lead.telefone = telefone
        self.db.session.commit()

    def delete_lead(self, lead_id):
        lead = self.get_lead_by_id(lead_id)
        self.db.session.delete(lead)
        self.db.session.commit()
