from django.db import models


class CollectionRequest(models.Model):
    """
    CollectionRequest model
    """

    url = models.CharField(max_length=255)
    file = models.FileField(upload_to="collection_requests")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collection request #{self.id}"
