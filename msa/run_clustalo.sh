#!/bin/bash
clustalo -i fasta_by_chain.fasta -o chains_alignment.aln --outfmt=clu --force --resno --output-order=tree-order --wrap=120 --distmat-out=distance.matrix --guidetree-out=guide.tree --clustering-out=clustering.out --full
