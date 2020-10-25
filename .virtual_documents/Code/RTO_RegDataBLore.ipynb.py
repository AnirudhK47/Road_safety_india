import tabula


filea_path = 'VUB - 17.pdf'
fileb_path = 'VUB - 18.pdf'
filec_path = 'VUB - 19.pdf'


dfa = tabula.read_pdf(filea_path,lattice = True,pages=1,multiple_tables=False)
dfb = tabula.read_pdf(fileb_path,lattice = True,pages=1,multiple_tables=False)
dfc = tabula.read_pdf(filec_path,lattice = True,pages=1,multiple_tables=False)


dfx = dfa[0]
dfy = dfb[0]
dfz = dfc[0]


dfx



