outfile = open("GenomeWideSNP_6.na35.anno.info.txt", "w")
outfile.write("\t".join(["ID", "pos_id", "info"]) + "\n")

with open("GenomeWideSNP_6.na35.annot.csv") as csvfile:
	header = True
	nline = 0
	for line in csvfile:
		linelist = line[:-1].split(",")
		if linelist[0][0] != "#":
			if header:
				header = False
			else:
				nline += 1
				sid = linelist[0].split("_")[-1].strip('"')
				chrom = "chr" + linelist[2].strip('"')
				pos = linelist[3].strip('"')
				rsid = "NOVEL" if linelist[1].strip('"')[0] == "-" else linelist[1].strip('"')
				ref = linelist[8].strip('"')
				alt = linelist[9].strip('"')

				# if chrom[0].strip('"') == "-" or pos[0].strip('"') == "-":
				# 	continue

				pos_id = "_".join([chrom, pos, rsid, ref, alt])

				infoline = ""
				if linelist[10][0].strip('"') != '-':
					gene_list = linelist[10].strip('"').split("///")
					for genes in gene_list:
						gene_info_list = genes.split("//")
						# print("nline: " + str(nline))
						# print(gene_info_list[4].strip())
						if len(gene_info_list) < 4:
							continue
						if gene_info_list[4].strip()[0] != '-':
							gene_name = gene_info_list[4].strip()
							gene_pos = gene_info_list[1].strip()
							gene_info = gene_info_list[6].strip()
							infoline += ';'.join([gene_name, gene_pos, gene_info]) + "|"

				outline = "\t".join([sid, pos_id, infoline]) + "\n"

				outfile.write(outline)