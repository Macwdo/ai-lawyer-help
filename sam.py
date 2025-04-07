from ai.services.pdf_manager import PDFFeedManager
from common.models import File


mngr = PDFFeedManager()


file = File.objects.get(code="134487637CD5")
mngr.extract(file)
