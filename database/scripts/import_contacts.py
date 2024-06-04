import csv
from database.config import SessionLocal
from models.contact import Contact


def import_contacts(file_path):
    session = SessionLocal()
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        next(reader)
        for row in reader:
            _id, name = row
            contact = session.get(Contact, int(_id))
            if contact:
                contact.name = name.strip()
            else:
                contact = Contact(id=int(_id), name=name.strip())
                session.add(contact)
    session.commit()
    session.close()


if __name__ == "__main__":
    import_contacts("*task/contacts.txt")
    print("Imported contacts")
