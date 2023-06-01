from django.db import models


class CollectionRequest(models.Model):
    """
    CollectionRequest model
    """

    file = models.FileField(upload_to="collection_requests", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collection request #{self.id}"
