from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.include('pyramid_debugtoolbar')
    # home
    config.add_route('index', '/')
    # Documentos da Colecao:
    config.add_route('collection_documents', '/api/v1/collection/{collection_acronym}/document/')
    # Documentos do Periodico:
    config.add_route('journal_documents', '/api/v1/journal/{journal_issn}/document/')
    # Citacoes da Colecao:
    config.add_route('collection_citations', '/api/v1/collection/{collection_acronym}/citation/')
    # Citacoes do Periodico:
    config.add_route('journal_citations', '/api/v1/journal/{journal_issn}/citation/')
    config.scan()
    return config.make_wsgi_app()
