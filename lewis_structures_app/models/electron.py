from django.db import models

# from .atom import Atom


class Electron(models.Model):
    electron_id = models.BigAutoField(primary_key=True)
    starting_is_paired = models.BooleanField(default=False, blank=True)
    is_paired = models.BooleanField(default=None, blank=True)
    atom = models.ForeignKey("lewis_structures_app.Atom", on_delete=models.CASCADE)
    # paired_with = models.IntegerField(default=None, blank=True)
    # paired_with = models.ForeignKey("lewis_structures_app.Electron", default=None, blank=True, on_delete=models.CASCADE)
    # front end may be able to handle this:
    # bonded_to = models.IntegerField("Electron id bonded to")

    def to_dict(self):
        # is_paired = False
        # if (self.paired_with is not None):
        #     is_paired = True
        electron = {
            "electron_id": self.electron_id,
            "is_paired": self.is_paired,
            # b/c its serialized
            "atom": self.atom,
            # "paired_with": self.paired_with
        }

    def update(self, req_body):

        self.atom = req_body["atom"]
        self.is_paired = req_body["is_paired"]
        # self.paired_with = req_body["paired_with"]

    # initializing the class/creating an instance
    @classmethod
    def create(cls, req_body):
        electron = cls(
            atom=req_body["atom"],
            # atom=Atom.get(req_body["atom"])
            # slower and requires an extra database request
            is_paired=req_body["is_paired"],
            # paired_with=req_body["paired_with"]
        )
        return electron

    # @electron_bp.route("/<id>", methods=["PUT"])
    # def update_electron(id):
    #     # electron = validate_electron(id)

    #     request_body = request.get_json()

    #     electron.update(request_body)

    #     db.session.commit()

    #     return jsonify(electron.to_dict()), 200
