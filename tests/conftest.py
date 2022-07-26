import pytest
from lewis_structures_app import db
from lewis_structures_app.models.atom import Electron
from lewis_structures_app.models.atom import Atom
from lewis_structures_app.models.atom import Molecule

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def hydrogen_atom_H2_molecule(app):
    H2 = Molecule(molecular_formula="H2")
    db.session.add(H2)
    db.session.commit()

    H = Atom(element_symbol="H", molecule="1")
    db.session.add(H)
    db.session.commit()

    
    



