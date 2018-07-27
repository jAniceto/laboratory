AUTHOR_LIST = ['Da Silva, Francisco',
               'Silva, Carlos Manuel',
               'Xavier, Ana Maria Rebelo Barreto',
               'Portugal, Inês',
               'Margarida Barros, Ana',
               'Pascoal-Neto, Carlos',
               'Serafim, Luísa S.',
               'Valente, Anabela A.',
               'Ventura, Sónia P.M.',
               'Carvalho, Pedro J.',
               'Freire, Mara G.',
               'Mano, João Filipe Colardelle Da Luz',
               'Coutinho, João A.P.',
               'Evtyugin, Dmitry V.']


ORCID_LIST = ['0000-0002-6304-5105',
              '0000-0003-3495-2133',
              '0000-0001-9049-4267',
              '0000-0002-1943-0006',
              '0000-0001-8895-0614',
              '0000-0002-2342-3765',
              '0000-0002-3841-743X',
              '0000-0001-7339-7019',
              '0000-0003-0767-721X',
              '0000-0002-6462-8679',
              '0000-0002-9310-2457',
              '0000-0002-0522-8069',
              '0000-0001-5802-1777',
              '0000-0002-8562-9275'] 

SCOPUSID_LIST = ['7004261144',
                 '7102410108',
                 '16418060900',
                 '55977169000',
                 '57200173922',
                 '26643558900',
                 '56962705900',
                 '7102042412',
                 '15132924000',
                 '6506756470',
                 '57195637544',
                 '7102758259',
                 '6603046030',
                 '7005164431']

query_orcid = ''
for orcid in ORCID_LIST:
    query_orcid += 'ORCID({}) OR '.format(orcid)

query_scopusid = ''
for scopusid in SCOPUSID_LIST:
    query_scopusid += 'AU-ID({}) OR '.format(scopusid)

print(query_scopusid)