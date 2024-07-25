from django.db import models
from import_export import resources


# Create your models here.

class lote(models.Model):
    codigo = models.CharField(max_length=11, primary_key=True)
    manzana = models.IntegerField(default=0, null=True, blank=True)
    lote = models.IntegerField(default=0, null=True, blank=True)
    estado = models.CharField(max_length=10)
    fecha = models.DateField("fecha", null=True, blank=True)
    vendedor = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"Lote {self.lote} in Manzana {self.manzana} (Código: {self.codigo}), " f"Estado: {self.estado},  "f"Vendedor: {self.vendedor}"

    def formatted_date(self):
        if self.date_field:
            return self.date_field.strftime('%m-%d-%Y')
        return 'N/A'  # or any other placeholder for None values


class loteResource(resources.ModelResource):
    class Meta:
        model = lote
        import_fields = ["codigo"]
        skip_unchanged = True
        use_bulk = True
