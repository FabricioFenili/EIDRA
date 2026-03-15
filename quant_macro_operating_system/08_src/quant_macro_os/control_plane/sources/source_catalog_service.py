from quant_macro_os.control_plane.sources.source_catalog import SOURCE_CATALOG
class SourceCatalogService:
    def list_templates(self):
        return [value for _, value in sorted(SOURCE_CATALOG.items(), key=lambda item: item[0])]
    def list_template_names(self):
        return sorted(SOURCE_CATALOG.keys())
    def get_template(self, template_name):
        return SOURCE_CATALOG[template_name]
    def list_categories(self):
        return sorted({value["category"] for value in SOURCE_CATALOG.values()})
