from CollectionsData import table_Manager
from CollectionsData import table_Staff
from CollectionsData import table_Menu
from CollectionsData import table_Orders
from CollectionsData import table_Reservations


# Create collection with schema
def create_collection_with_fields(db, collection_name, schema):
    validator = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": list(schema.keys()),
            "properties": {
                field: {"bsonType": details["type"]} for field, details in schema.items()
            }
        }
    }
    db.create_collection(
        collection_name,
        validator=validator
    )

# Create the database collections
def create_database(DB): 

    # Create the collections
    create_table_Manager(DB)
    create_table_Staff(DB)
    create_table_Menu(DB)
    create_table_Orders(DB)
    create_table_Reservations(DB)

    return DB

# Create the tables

# Create the Manager table
def create_table_Manager(db):
    if "Manager" in db.list_collection_names():
        db.drop_collection("Manager")
    create_collection_with_fields(db, "Manager", table_Manager)

# Create the Staff table
def create_table_Staff(db):
    if "Staff" in db.list_collection_names():
        db.drop_collection("Staff")
    create_collection_with_fields(db, "Staff", table_Staff)

# Create the Menu table
def create_table_Menu(db):
    if "Menu" in db.list_collection_names():
        db.drop_collection("Menu")
    create_collection_with_fields(db, "Menu", table_Menu)

# Create the Orders table
def create_table_Orders(db):
    if "Orders" in db.list_collection_names():
        db.drop_collection("Orders")
    create_collection_with_fields(db, "Orders", table_Orders)

# Create the Reservations table
def create_table_Reservations(db):
    if "Reservations" in db.list_collection_names():
        db.drop_collection("Reservations")
    create_collection_with_fields(db, "Reservations", table_Reservations)

