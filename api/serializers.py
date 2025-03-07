from rest_framework import serializers


class CodeRelatedField(serializers.SlugRelatedField):
    def __init__(self, *, model, **kwargs):
        queryset = model.objects.all()
        kwargs["queryset"] = queryset
        super().__init__(slug_field="code", write_only=True, **kwargs)


class CodeRelatedFieldByLawfirm(CodeRelatedField):
    def __init__(self, *, model, **kwargs):
        queryset = model.objects.all().filter(lawfirm=self.context["lawfirm"])
        kwargs["queryset"] = queryset
        super().__init__(model=model, **kwargs)
