class Warehouse:
    def __init__(self, id, code, name, address, zip, city, province, country, contact, created_at, updated_at):
        self.id = id
        self.code = code
        self.name = name
        self.address = address
        self.zip = zip
        self.city = city
        self.province = province
        self.country = country
        self.contact = contact  ## contact contains contact_name, contact_email, contact_phone
        self.created_at = created_at
        self.updated_at = updated_at
