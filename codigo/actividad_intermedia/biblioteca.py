#####################################################
# datos para el ejercicio intermedio
# biblioteca
# autor: Jairo Antonio Melo Flórez
# fecha: 2023-03-26
# version: 1.0
# licencia: MIT License
#####################################################

import requests
import json
import os

# ubicar este archivo en la raiz del proyecto

biblioteca = [
	{
		"id": "http://zotero.org/users/163570/items/32TCDQ2T",
		"type": "book",
		"collection-title": "Blackwell Companions to Literature and Culture",
		"event-place": "Oxford",
		"ISBN": "1-4051-0321-3",
		"publisher": "Blackwell Publishing Professional",
		"publisher-place": "Oxford",
		"title": "Companion to Digital Humanities",
		"URL": "http://www.digitalhumanities.org/companion/",
		"author": [
			{
				"family": "Schreibman",
				"given": "Susan"
			},
			{
				"family": "Siemens",
				"given": "Ray"
			},
			{
				"family": "Unsworth",
				"given": "John"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2004",
					12
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RBT5F3UV",
		"type": "webpage",
		"title": "Mining the Dispatch",
		"URL": "http://dsl.richmond.edu/dispatch/pages/intro",
		"author": [
			{
				"family": "Nelson",
				"given": "Robert K."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/P3HM63JW",
		"type": "webpage",
		"title": "MALLET homepage",
		"URL": "http://mallet.cs.umass.edu/",
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/H2F7J6S8",
		"type": "webpage",
		"container-title": "Google Ngram Viewer",
		"title": "Datasets",
		"URL": "http://storage.googleapis.com/books/ngrams/books/datasetsv2.html",
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5V3Q37X9",
		"type": "book",
		"abstract": "Besides familiar and now-commonplace tasks that computers do all the time, what else are they capable of? Stephen Ramsay's intriguing study of computational text analysis examines how computers can be used as \"reading machines\" to open up entirely new possibilities for literary critics. Computer-based text analysis has been employed for the past several decades as a way of searching, collating, and indexing texts. Despite this, the digital revolution has not penetrated the core activity of literary studies: interpretive analysis of written texts. Computers can handle vast amounts of data, allowing for the comparison of texts in ways that were previously too overwhelming for individuals, but they may also assist in enhancing the entirely necessary role of subjectivity in critical interpretation. Reading Machines discusses the importance of this new form of text analysis conducted with the assistance of computers. Ramsay suggests that the rigidity of computation can be enlisted in the project of intuition, subjectivity, and play.",
		"ISBN": "978-0-252-03641-5",
		"language": "en",
		"number-of-pages": "114",
		"publisher": "University of Illinois Press",
		"source": "Google Books",
		"title": "Reading Machines: Toward an Algorithmic Criticism",
		"title-short": "Reading Machines",
		"author": [
			{
				"family": "Ramsay",
				"given": "Stephen"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2011"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/DPQIFMVM",
		"type": "article-journal",
		"abstract": "Pensando en la pregunta sobre la muerte del libro como tema para este texto, me acordé de una conferencia dictada en 1998 por Umberto Eco en Venecia, en el marco de un curso dirigido a jóvenes libreros italianos. Dijo Eco: Estoy obsesionado desde hace algunos años por una pregunta planteada en cualquier entrevista o en cualquier coloquio donde estoy invitado; ¿qué piensa usted de la muerte del libro? No aguanto más el interrogante. Pero como empiezo a tener algunas ideas en cuanto a mi propia muerte entiendo bien que esta pregunta repetitiva traduce una verdadera y profunda inquietud.",
		"container-title": "Co-herencia",
		"ISSN": "1794-5887",
		"issue": "7",
		"language": "es",
		"license": "Copyright (c)",
		"page": "119-129",
		"source": "publicaciones.eafit.edu.co",
		"title": "¿La muerte del libro?",
		"URL": "http://publicaciones.eafit.edu.co/index.php/co-herencia/article/view/318",
		"volume": "4",
		"author": [
			{
				"family": "Chartier",
				"given": "Roger"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2007"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ISCPGW6D",
		"type": "article-journal",
		"container-title": "Revista signos",
		"DOI": "10.4067/S0718-09341999000100010",
		"ISSN": "0718-0934",
		"issue": "45-46",
		"page": "83-101",
		"source": "SciELO",
		"title": "La lectura en la Universidad de Antioquía: Informe preliminar",
		"title-short": "La lectura en la Universidad de Antioquía",
		"URL": "http://www.scielo.cl/scielo.php?script=sci_abstract&pid=S0718-09341999000100010&lng=es&nrm=iso&tlng=es",
		"volume": "32",
		"author": [
			{
				"family": "N",
				"given": "Castañeda"
			},
			{
				"family": "Stella",
				"given": "Luz"
			},
			{
				"family": "S",
				"given": "Henao"
			},
			{
				"family": "Ignacio",
				"given": "José"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"1999"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/G7DQC3JK",
		"type": "article-journal",
		"container-title": "Journal of Documentation",
		"DOI": "10.1108/00220410510632040",
		"ISSN": "0022-0418",
		"issue": "6",
		"journalAbbreviation": "Journal of Documentation",
		"page": "700-712",
		"source": "emeraldinsight.com (Atypon)",
		"title": "Reading behavior in the digital environment: Changes in reading behavior over the past ten years",
		"title-short": "Reading behavior in the digital environment",
		"URL": "http://www.emeraldinsight.com/doi/abs/10.1108/00220410510632040",
		"volume": "61",
		"author": [
			{
				"family": "Liu",
				"given": "Ziming"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2005"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/AUTFGGSI",
		"type": "book",
		"collection-number": "2",
		"collection-title": "Essays in hermeneutics",
		"event-place": "Evanston, Ill",
		"ISBN": "978-0-8101-0992-6",
		"language": "eng",
		"number-of-pages": "346",
		"publisher": "Northwestern University Press",
		"publisher-place": "Evanston, Ill",
		"source": "Gemeinsamer Bibliotheksverbund ISBN",
		"title": "From text to action",
		"author": [
			{
				"family": "Ricœur",
				"given": "Paul"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1991"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/GPIWJIGV",
		"type": "paper-conference",
		"event-place": "Balitmore",
		"event-title": "National Science Foundation Symposium on Next Generation of Data Mining and Cyber-Enabled Discovery for Innovation",
		"publisher-place": "Balitmore",
		"title": "The Remaking of Reading: Data Mining and the Digital Humanities",
		"URL": "http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.111.959&rep=rep1&type=pdf",
		"author": [
			{
				"family": "Kirschenbaum",
				"given": "Matthew G."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2007",
					10,
					10
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/XR9IP8HP",
		"type": "article-journal",
		"container-title": "Revista de lexicografía",
		"page": "9-28",
		"title": "Hacia una definición del concepto de colocación: de J. R. Firth a I. A. Mel'ĉuk",
		"title-short": "Hacia una definición del concepto",
		"volume": "1",
		"author": [
			{
				"family": "Alonso Ramos",
				"given": "Margarita"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1995"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BMM7QMVJ",
		"type": "article-journal",
		"abstract": "The idea that text in a particular field of discourse is organized into lexical patterns, which can be visualized as networks of words that collocate with each other, was originally proposed by Phillips (1983). This idea has important theoretical implications for our understanding of\nthe relationship between the lexis and the text and (ultimately) between the text and the discourse community/the mind of the speaker. Although the approaches to date have offered different possibilities for constructing collocation networks, we argue that they have not yet successfully operationalized\nsome of the desired features of such networks. In this study, we revisit the concept of collocation networks and introduce GraphColl, a new tool developed by the authors that builds collocation networks from user-defined corpora. In a case study using data from McEnery’s (2006a)\nstudy of the Society for the Reformation of Manners Corpus (SRMC), we demonstrate that collocation networks provide important insights into meaning relationships in language.",
		"container-title": "International Journal of Corpus Linguistics",
		"DOI": "10.1075/ijcl.20.2.01bre",
		"issue": "2",
		"journalAbbreviation": "International Journal of Corpus Linguistics",
		"page": "139-173",
		"source": "IngentaConnect",
		"title": "Collocations in context: A new perspective on collocation networks",
		"title-short": "Collocations in context",
		"volume": "20",
		"author": [
			{
				"family": "Brezina",
				"given": "Vaclav"
			},
			{
				"family": "McEnery",
				"given": "Tony"
			},
			{
				"family": "Wattam",
				"given": "Stephen"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/MKGFEWDQ",
		"type": "article-journal",
		"abstract": "<p>The tool <span class=\"jp-italic\">GraphColl</span> (Brezina et al. 2015) allows collocational networks to be identified within corpora, enabling corpus analysis to go beyond two-way collocation. This paper aims to illustrate the types of linguistic relationships that can appear when more than two words are considered, using graph theory to account for the different types of collocational “shapes” that can be formed within <span class=\"jp-italic\">GraphColl</span> networks. Using the reference corpus, the BE06, examples of different types of graphs were obtained and analysed in order to form an understanding of the sorts of relationships between words that occur in particular shapes. The analysis indicates that concepts from graph theory can be usefully integrated into corpus analysis of collocation as well as showing the potential for a more sophisticated understanding of the company that words keep.</p>",
		"container-title": "International Journal of Corpus Linguistics",
		"DOI": "10.1075/ijcl.21.2.01bak",
		"ISSN": "1384-6655, 1569-9811",
		"issue": "2",
		"language": "en",
		"page": "139-164",
		"source": "www.jbe-platform.com",
		"title": "The shapes of collocation",
		"URL": "http://www.jbe-platform.com/content/journals/10.1075/ijcl.21.2.01bak",
		"volume": "21",
		"author": [
			{
				"family": "Baker",
				"given": "Paul"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2018",
					2,
					18
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WTY3KR8Y",
		"type": "article-journal",
		"abstract": "Semantic change is a manifestation of the evolution of the semantic content of a word. We propose the study of semantic change linked to specific historical events and sociolinguistic situations, for example, the semantic connotations associated with everyday terms as España in various autonomous regions, demand its replacement by an euphemism Estado. Our hypothesis is that language adapts, if necessary, with an extraordinary agility to fulfill the need to express new, sometimes extraordinarily complex, realities not only through the use of neologisms (e.g., balompié), but also expanding, recycling or recreating the semantic load of heritage words (e.g., terrateniente). We propose to study and illustrate how language reflects the ideological and religious adherence of certain users of lexemes or word units (e.g., derechona, brotes verdes) and to provide, wherever possible, a link to the historical facts where they are born.",
		"container-title": "Itinerarios: revista de estudios lingüisticos, literarios, históricos y antropológicos",
		"ISSN": "1507-7241",
		"issue": "23",
		"language": "spa",
		"page": "123-139",
		"source": "dialnet.unirioja.es",
		"title": "El efecto de la historia sobre el cambio semántico en el español peninsular",
		"URL": "https://dialnet.unirioja.es/servlet/articulo?codigo=6163462",
		"author": [
			{
				"family": "Pazos-Bretaña",
				"given": "José-Manuel"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2018",
					2,
					17
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/B2349VQS",
		"type": "chapter",
		"container-title": "Debates in the Digital Humanities",
		"event-place": "Minneapolis",
		"page": "85-95",
		"publisher": "Universidad de Minnesota",
		"publisher-place": "Minneapolis",
		"title": "Humanistic Theory and Digital Scholarship",
		"URL": "http://dhdebates.gc.cuny.edu/debates/text/34",
		"author": [
			{
				"family": "Drucker",
				"given": "Johanna"
			}
		],
		"editor": [
			{
				"family": "Gold",
				"given": "Matthew"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/84T93FAC",
		"type": "article-journal",
		"collection-title": "II",
		"container-title": "New Left Review",
		"ISSN": "0028-6060",
		"issue": "24",
		"journalAbbreviation": "NLR",
		"page": "67-93",
		"title": "Graphs, Maps, Trees - 1",
		"author": [
			{
				"family": "Moretti",
				"given": "Franco"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2003"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5JSX7FHP",
		"type": "webpage",
		"container-title": "the scottbot irregular",
		"language": "English",
		"title": "\"Digital History\" Can Never Be New",
		"URL": "http://scottbot.net/digital-history-can-never-be-new/",
		"author": [
			{
				"family": "Weingart",
				"given": "Scott"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					19
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016",
					5,
					2
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BBETWKRX",
		"type": "article-journal",
		"container-title": "Historia Crítica",
		"issue": "43",
		"page": "38-61",
		"title": "“Guardar como”. La historia y las fuentes digitales",
		"title-short": "Guardar como",
		"author": [
			{
				"family": "Pons",
				"given": "Anaclet"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2011"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/T5VS34K4",
		"type": "post-weblog",
		"container-title": "Essays on History and New Media",
		"genre": "Roy Rosenzweig Center for History and New Media",
		"title": "Why Collecting History Online is Web 1.5",
		"URL": "http://chnm.gmu.edu/essays-on-history-new-media/essays/?essayid=47",
		"author": [
			{
				"family": "Brennan",
				"given": "Sheila A."
			},
			{
				"family": "Kelly",
				"given": "T. Mills"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2015",
					3,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2009"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/APFAHS6C",
		"type": "post-weblog",
		"title": "Scripto",
		"URL": "http://scripto.org/",
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					16
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JWBGBU4Z",
		"type": "webpage",
		"title": "How do you define Humanities Computing / Digital Humanities? - Taporwiki",
		"URL": "http://www.artsrn.ualberta.ca/taporwiki/index.php/How_do_you_define_Humanities_Computing_/_Digital_Humanities%3F",
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					16
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/XHIUAZC6",
		"type": "webpage",
		"title": "Archivo de Publicidad Colombiana 1800-1950",
		"URL": "http://apc.historiaabierta.org/",
		"accessed": {
			"date-parts": [
				[
					"2016",
					5,
					19
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/93RVDA7Z",
		"type": "webpage",
		"container-title": "Dh2015.org",
		"title": "What Do You Do With A Million Readers?",
		"URL": "http://dh2015.org/abstracts/xml/TANGHERLINI_Timothy_Roland_What_Do_You_Do_With_A_/TANGHERLINI_Timothy_Roland_What_Do_You_Do_With_A_Millio.html",
		"author": [
			{
				"family": "Bandari",
				"given": "Roja"
			},
			{
				"family": "Tangherlini",
				"given": "Timothy Roland"
			},
			{
				"family": "Roychowdhury",
				"given": "Vwani"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					19
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015",
					7,
					3
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6PXF56QV",
		"type": "article-journal",
		"container-title": "D-Lib Magazine",
		"DOI": "10.1045/march2006-crane",
		"ISSN": "1082-9873",
		"issue": "3",
		"language": "en",
		"source": "CrossRef",
		"title": "What Do You Do with a Million Books?",
		"URL": "http://www.dlib.org/dlib/march06/crane/03crane.html",
		"volume": "12",
		"author": [
			{
				"family": "Crane",
				"given": "Gregory"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					19
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2006",
					3
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6HJC86ZI",
		"type": "post-weblog",
		"abstract": "Stuart Dunn examines the development of crowd-sourcing activities in academic contexts and identifies the potential for looking beyond the short-term benefits crowd-sourcing offers to a project’s c…",
		"container-title": "Impact of Social Sciences",
		"title": "More than a business model: crowd-sourcing and impact in the humanities",
		"title-short": "More than a business model",
		"URL": "http://blogs.lse.ac.uk/impactofsocialsciences/2013/03/21/more-than-a-business-model-crowd-sourcing-and-impact-in-the-humanities/",
		"author": [
			{
				"family": "Dunn",
				"given": "Stuart"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					19
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2013",
					3,
					21
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6XRMW7P8",
		"type": "webpage",
		"abstract": "Crowdsourcing: participatory digital research methods",
		"genre": "Page",
		"language": "en",
		"title": "Crowdsourcing — Digital Humanities Network",
		"URL": "http://www.digitalhumanities.cam.ac.uk/Methods/Crowdsourcing",
		"author": [
			{
				"family": "raa43@cam.ac.uk",
				"given": ""
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					19
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BUN8QC2B",
		"type": "post-weblog",
		"abstract": "Crowdsourcing is rather broadly defined term. First coined in 2006 as a portmanteau of the words “crowd” and “outsourcing”, it refers to “the practice of obtaining needed services, ideas or content…",
		"container-title": "DH101",
		"title": "The Potential of Crowdsourcing for Digital Humanities Research",
		"URL": "https://dh101.ch/2015/10/20/the-potential-of-crowd-sourcing-for-digital-humanities-research/",
		"author": [
			{
				"family": "SL",
				"given": "Mr"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					19
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015",
					10,
					20
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6XSHDKIT",
		"type": "post-weblog",
		"abstract": "The web is an archive that is constantly changing and effectively infinite. What kind of research techniques can historians develop to make use of it? There are already a number of excellent resour…",
		"container-title": "William J Turkel",
		"title": "2005-12-18 Digital History Hacks",
		"URL": "https://williamjturkel.net/digital-history-hacks-2005-08/2005-12-18-digital-history-hacks/",
		"author": [
			{
				"family": "Turkel",
				"given": "William J."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					5,
					29
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2012",
					4,
					17
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7RTBCDSJ",
		"type": "webpage",
		"abstract": "Profesor en Stanford, el académico italiano, hermano de Nanni, el cineasta, aplica la \"crítica computacional\" para analizar la literatura",
		"title": "Franco Moretti: \"El estudio de la cultura perdió mucho por no seguir un método científico\"",
		"title-short": "Franco Moretti",
		"URL": "http://www.lanacion.com.ar/1828487-franco-moretti-el-estudio-de-la-cultura-perdio-mucho-por-no-seguir-un-metodo-cientifico",
		"accessed": {
			"date-parts": [
				[
					"2016",
					5,
					29
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/EWNCWU3N",
		"type": "post-weblog",
		"title": "Stanford Literary Lab – Directed by Franco Moretti and Mark Algee-Hewitt",
		"URL": "http://litlab.stanford.edu/",
		"accessed": {
			"date-parts": [
				[
					"2016",
					5,
					28
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/DCKU7CB7",
		"type": "book",
		"event-place": "London, New York",
		"ISBN": "978-1-84467-185-4",
		"language": "eng",
		"note": "OCLC: 845372315",
		"number-of-pages": "119",
		"publisher": "Verso",
		"publisher-place": "London, New York",
		"source": "Gemeinsamer Bibliotheksverbund ISBN",
		"title": "Graphs, maps, trees: abstract models for literary history",
		"title-short": "Graphs, maps, trees",
		"author": [
			{
				"family": "Moretti",
				"given": "Franco"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2007"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/W4GRU9WP",
		"type": "book",
		"call-number": "P93 .K74 2004",
		"edition": "2nd ed",
		"event-place": "Thousand Oaks, Calif",
		"ISBN": "978-0-7619-1544-7",
		"number-of-pages": "413",
		"publisher": "Sage",
		"publisher-place": "Thousand Oaks, Calif",
		"source": "Library of Congress ISBN",
		"title": "Content analysis: an introduction to its methodology",
		"title-short": "Content analysis",
		"author": [
			{
				"family": "Krippendorff",
				"given": "Klaus"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2004"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/8N26EF75",
		"type": "book",
		"event-place": "Buenos Aires",
		"ISBN": "978-987-719-090-8",
		"number-of-pages": "274",
		"publisher": "Fondo de Cultura Económica",
		"publisher-place": "Buenos Aires",
		"title": "Lectura distante",
		"author": [
			{
				"family": "Moretti",
				"given": "Franco"
			}
		],
		"translator": [
			{
				"family": "Mosconi",
				"given": "Lilia"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RK5J5RMF",
		"type": "webpage",
		"genre": "Digital Humanities Now",
		"title": "About",
		"URL": "http://digitalhumanitiesnow.org/about/",
		"author": [
			{
				"literal": "Digital Humanities Now"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					8,
					29
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9EMADB3D",
		"type": "article-journal",
		"container-title": "O’Reilly Media",
		"title": "What Is Web 2.0. Design Patterns and Business Models for the Next Generation of Software",
		"URL": "http://www.oreilly.com/pub/a/web2/archive/what-is-web-20.html",
		"author": [
			{
				"family": "O'Reilly",
				"given": "Tim"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2005"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RUFGI24G",
		"type": "article-journal",
		"abstract": "We constructed a corpus of digitized texts containing about 4% of all books ever printed. Analysis of this corpus enables us to investigate cultural trends quantitatively. We survey the vast terrain of \"culturomics\", focusing on linguistic and cultural phenomena that were reflected in the English language between 1800 and 2000. We show how this approach can provide insights about fields as diverse as lexicography, the evolution of grammar, collective memory, the adoption of technology, the pursuit of fame, censorship, and historical epidemiology. \"Culturomics\" extends the boundaries of rigorous quantitative inquiry to a wide array of new phenomena spanning the social sciences and the humanities.",
		"container-title": "Science",
		"DOI": "10.1126/science.1199644",
		"ISSN": "0036-8075, 1095-9203",
		"language": "en",
		"license": "Copyright © 2010, American Association for the Advancement of Science",
		"note": "PMID: 21163965",
		"page": "1199644",
		"source": "science.sciencemag.org",
		"title": "Quantitative Analysis of Culture Using Millions of Digitized Books",
		"URL": "http://science.sciencemag.org/content/early/2010/12/15/science.1199644",
		"author": [
			{
				"family": "Michel",
				"given": "Jean-Baptiste"
			},
			{
				"family": "Shen",
				"given": "Yuan Kui"
			},
			{
				"family": "Aiden",
				"given": "Aviva P."
			},
			{
				"family": "Veres",
				"given": "Adrian"
			},
			{
				"family": "Gray",
				"given": "Matthew K."
			},
			{
				"family": "Team",
				"given": "The Google Books"
			},
			{
				"family": "Pickett",
				"given": "Joseph P."
			},
			{
				"family": "Hoiberg",
				"given": "Dale"
			},
			{
				"family": "Clancy",
				"given": "Dan"
			},
			{
				"family": "Norvig",
				"given": "Peter"
			},
			{
				"family": "Orwant",
				"given": "Jon"
			},
			{
				"family": "Pinker",
				"given": "Steven"
			},
			{
				"family": "Nowak",
				"given": "Martin A."
			},
			{
				"family": "Aiden",
				"given": "Erez Lieberman"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2016",
					6,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2010",
					12,
					16
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VW6NHF99",
		"type": "article-journal",
		"abstract": "We introduce the Word Tree, a new visualization and information-retrieval technique aimed at text documents. A word tree is a graphical version of the traditional \"keyword-in-context\" method, and enables rapid querying and exploration of bodies of text. In this paper we describe the design of the technique, along with some of the technical issues that arise in its implementation. In addition, we discuss the results of several months of public deployment of word trees on Many Eyes, which provides a window onto the ways in which users obtain value from the visualization.",
		"container-title": "IEEE transactions on visualization and computer graphics",
		"DOI": "10.1109/TVCG.2008.172",
		"ISSN": "1077-2626",
		"issue": "6",
		"journalAbbreviation": "IEEE Trans Vis Comput Graph",
		"language": "eng",
		"note": "PMID: 18988967",
		"page": "1221-1228",
		"source": "PubMed",
		"title": "The Word Tree, an interactive visual concordance",
		"volume": "14",
		"author": [
			{
				"family": "Wattenberg",
				"given": "Martin"
			},
			{
				"family": "Viégas",
				"given": "Fernanda B."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2008"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/N6TZIIK3",
		"type": "paper-conference",
		"container-title": "DH2018 Abstracts",
		"event-place": "México",
		"event-title": "Digital Humanities Conference",
		"language": "es-ES",
		"publisher-place": "México",
		"title": "Distributions of Function Words Across Narrative Time in 50,000 Novels",
		"title-short": "Distributions of Function Words",
		"URL": "https://dh2018.adho.org/distributions-of-function-words-across-narrative-time-in-50000-novels/",
		"author": [
			{
				"family": "McClure",
				"given": "David William"
			},
			{
				"family": "Enderle",
				"given": "Scott"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2018",
					12,
					18
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/H9MLI3U4",
		"type": "webpage",
		"title": "Towards a Taxonomy of Failure | Quinn Dombrowski",
		"URL": "https://www.quinndombrowski.com/?q=blog/2019/01/30/towards-taxonomy-failure",
		"accessed": {
			"date-parts": [
				[
					"2019",
					2,
					26
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/LM838CNV",
		"type": "book",
		"abstract": "Scholars of all stripes are turning their attention to materials that represent enormous opportunities for the future of humanistic inquiry. The purpose of this book is to impart the concepts that underlie the mathematics they are likely to encounter and to unfold the notation in a way that removes that particular barrier completely. This book is a primer for developing the skills to enable humanist scholars to address complicated technical material with confidence. This book, to put it plainly, is concerned with the things that the author of a technical article knows, but isn't saying. Like any field, mathematics operates under a regime of shared assumptions, and it is our purpose to elucidate some of those assumptions for the newcomer. The individual subjects we tackle are (in order): logic and proof, discrete mathematics, abstract algebra, probability and statistics, calculus, and differential equations.",
		"event-place": "Lincoln",
		"ISBN": "978-1-60962-111-7",
		"language": "English",
		"note": "OCLC: 1015817392",
		"publisher": "Zea E-Books",
		"publisher-place": "Lincoln",
		"source": "Open WorldCat",
		"title": "Six Septembers: mathematics for the humanist",
		"title-short": "Six Septembers",
		"author": [
			{
				"family": "Juola",
				"given": "Patrick"
			},
			{
				"family": "Ramsay",
				"given": "Stephen"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/47YPDCT4",
		"type": "article-journal",
		"container-title": "Signa: Revista de la Asociación Española de Semiótica",
		"ISSN": "1133-3634",
		"issue": "25",
		"language": "es",
		"page": "121-136",
		"title": "La evaluación de los recursos digitales para las humanidades",
		"URL": "https://dialnet.unirioja.es/servlet/articulo?codigo=5476765",
		"author": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2019",
					7,
					7
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JXGWH98A",
		"type": "book",
		"call-number": "PN4560.3 .L58 2018",
		"event-place": "Chicago ; London",
		"ISBN": "978-0-226-45181-7",
		"number-of-pages": "318",
		"publisher": "The University of Chicago Press",
		"publisher-place": "Chicago ; London",
		"source": "Library of Congress ISBN",
		"title": "Friending the past: the sense of history in the digital age",
		"title-short": "Friending the past",
		"author": [
			{
				"family": "Liu",
				"given": "Alan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/8KTPUEZ5",
		"type": "book",
		"event-place": "México",
		"language": "es",
		"number-of-pages": "209",
		"publisher": "Siglo XXI",
		"publisher-place": "México",
		"title": "Atlas de la novela europea, 1800-1900",
		"title-short": "Atlas de la novela",
		"author": [
			{
				"family": "Moretti",
				"given": "Franco"
			}
		],
		"translator": [
			{
				"family": "Mastrángelo",
				"given": "Stella",
				"suffix": ""
			}
		],
		"issued": {
			"date-parts": [
				[
					"1999"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/76W9SSTA",
		"type": "article-journal",
		"collection-title": "Second Series",
		"container-title": "New Left Review",
		"language": "eng",
		"page": "86-115",
		"title": "Hidden in Plain Sight. Data Visualization in the Humanities",
		"title-short": "Hidden in Plain Sight",
		"volume": "118",
		"author": [
			{
				"family": "Moretti",
				"given": "Franco"
			},
			{
				"family": "Sobchuk",
				"given": "Oleg"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/UL6ESGLD",
		"type": "paper-conference",
		"abstract": "This panel undertakes a speculative and theoretical discussion of possible future directions for digital humanities work driven by what we call informating, augmenting and automating technologies in the digital humanities. The panel particularly examines the emergence of a new paradigm of artificial intelligence around machine learning, statistical techniques and textual interfaces; a paradigm that challenges the way in which we understand the provision of digital humanities technologies and infrastructures. We explore the debates over informating, augmenting and automating processes that are now starting to emerge in digital humanities, and the historical trajectory that led to the current rapid changes from computational techniques. By looking at how machine-learning infrastructures effect knowledge formations, we engage with these new knowledges and practices, and argue that digital humanities must seek to contest and transform particular institutional structures that are problematic for humanities scholarship. Although differences have emerged within the digital humanities between “those who use new digital tools to aid relatively traditional scholarly projects and those who believe that DH is most powerful as a disruptive political force that has the potential to reshape fundamental aspects of academic practice” (Gold, 2012: x), it is still the case that, as a growing and developing disciplinary area, digital humanities has much opportunity for these disparate elements to work together. Not unlike differences between empirical and critical sociology in a previous iteration of a contestation over knowledge, epistemology, disciplinary identity and research, digital humanities as a discipline will be richer and more vibrant with alternative voices contributing to projects, publications and practices. Indeed, the debates within digital humanities “bear the mark of a field in the midst of growing pains as its adherents expand from a small circle of like-minded scholars to a more heterogeneous set of practitioners who sometimes ask more disruptive questions” (Gold, 2012: x-xi). Developing a critical approach to machine learning, for example, calls for computation itself to be historicised, and its developing relationship with humanities to be carefully uncovered. Similarly, by focusing on the materiality of machine learning, our attention is drawn to the microanalysis required at the level of computational conditions of possibility, combined with a macroanalysis of deployment of machine-learning systems in humanities work. This calls for us to think critically about how machine learning is being designed and deployed in the specific problem domains represented by the informating, augmenting and automating of digital humanities. The panel critically engages with these three modes of thought and practice, in order to connect and explore the present and possible future of digital humanities. We develop this approach in the context of these new techniques of knowledge-presentation, new infrastructures for knowledge work, and new formations around human capacities to work with complex and large data sets. Strong claims are often made about the potential for replacing aspects of traditionally humanities work undertaken by human labour alone through machinelearning techniques. Here, through a critical examination of new epistemologies and machine-generated data ontologies, for example, we examine the possibility of methods for a critical digital humanities in relation to new machine-learning techniques, together with how machine learning might be repurposed for a critical project within DH scholarship.",
		"container-title": "DH2017 Abstracts",
		"source": "Semantic Scholar",
		"title": "Critical Digital Humanities and Machine-Learning",
		"author": [
			{
				"family": "Bassett",
				"given": "Caroline"
			},
			{
				"family": "Berry",
				"given": "David M."
			},
			{
				"family": "Fazi",
				"given": "M. Beatrice"
			},
			{
				"family": "Pay",
				"given": "Jack"
			},
			{
				"family": "Roberts",
				"given": "Ben"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/MD7D7VS2",
		"type": "article-journal",
		"abstract": "This essay positions the use of machine learning within the digital humanities as part of a wider movement that nostalgically seeks to return literary criticism to the structuralist era, to a moment characterized by belief in systems, structure, and the transparency of language. It argues that the scientific criticism of the present attempts to separate methodology from interpretation and in the process it has deemphasized the degree to which methodology also participates in interpretation. This essay returns to the deconstructive critique of structuralism in order to highlight the ways in which numerous interpretive decisions are suppressed in the pre-processing of text and in the use of machine learning algorithms.",
		"container-title": "College Literature",
		"DOI": "10.1353/lit.2015.0037",
		"ISSN": "1542-4286",
		"issue": "4",
		"language": "en",
		"note": "publisher: Johns Hopkins University Press",
		"page": "543-564",
		"source": "Project MUSE",
		"title": "Can An Algorithm Be Disturbed?: Machine Learning, Intrinsic Criticism, and the Digital Humanities",
		"title-short": "Can An Algorithm Be Disturbed?",
		"URL": "https://muse.jhu.edu/article/595031",
		"volume": "42",
		"author": [
			{
				"family": "Dobson",
				"given": "James E."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2020",
					7,
					31
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015",
					10,
					6
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/A6SVA5MZ",
		"type": "article-journal",
		"abstract": "Computing and the use of digital sources and resources is an everyday and essential practice in current academic scholarship. The present article gives a concise overview of approaches and methods within digital historical scholarship, focusing on the question ‘How have the digital humanities evolved and what has that evolution brought to historical scholarship?’ We begin by discussing techniques in which data are generated and machine searchable, such as OCR/HTR, born-digital archives, computer vision, scholarly editions and linked data. In the second section, we provide examples of how data is made more accessible through quantitative text and network analysis. The third section considers the need for hermeneutics and data-awareness in digital historical scholarship. The technologies described in this article have had varying degrees of effect on historical scholarship, usually in indirect ways. With this article we aim to take stock of the digital approaches and methods used in historical scholarship in order to provide starting points for scholars seeking to understand the digital turn in the field and how and when to implement such approaches in their work.",
		"container-title": "History",
		"DOI": "10.1111/1468-229X.12969",
		"ISSN": "1468-229X",
		"issue": "365",
		"language": "en",
		"note": "_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1111/1468-229X.12969",
		"page": "291-312",
		"source": "Wiley Online Library",
		"title": "State of the Field: Digital History",
		"title-short": "State of the Field",
		"URL": "https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-229X.12969",
		"volume": "105",
		"author": [
			{
				"family": "Romein",
				"given": "C. Annemieke"
			},
			{
				"family": "Kemman",
				"given": "Max"
			},
			{
				"family": "Birkholz",
				"given": "Julie M."
			},
			{
				"family": "Baker",
				"given": "James"
			},
			{
				"family": "Gruijter",
				"given": "Michel De"
			},
			{
				"family": "Meroño‐Peñuela",
				"given": "Albert"
			},
			{
				"family": "Ries",
				"given": "Thorsten"
			},
			{
				"family": "Ros",
				"given": "Ruben"
			},
			{
				"family": "Scagliola",
				"given": "Stefania"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2020",
					9,
					3
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BWWWQKTY",
		"type": "post-weblog",
		"container-title": "Melissa Terras' Blog",
		"title": "Peering Inside the Big Tent: Digital Humanities and the Crisis of Inclusion",
		"title-short": "Melissa Terras' Blog",
		"URL": "http://melissaterras.blogspot.com/2011/07/peering-inside-big-tent-digital.html",
		"author": [
			{
				"family": "Terras",
				"given": "Melissa"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2020",
					11,
					16
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2011",
					7,
					26
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/YIJRQI3M",
		"type": "article-journal",
		"abstract": "The digital era has not only given us the world of big data, but the tools to deal with this mostly unstructured, mostly textual data: Natural Language Processing (NLP) tools. Yet, most humanists and social scientists do not work with big data. They do not deal with millions of documents. Literary critics’ corpora are the handful of works produced by an author. The historians’ primary source documents number in the tens, perhaps hundreds. Social scientists deal with tens or hundreds of transcripts of focus groups and in-depth interviews, or at most a few thousand media articles. And they analyze these data either qualitatively or quantitatively with a variety of manual or computer-assisted methodologies, from content analysis to frame analysis, discourse analysis, quantitative narrative analysis. But, once developed, at least some of the NLP tools of automatic textual analysis and the data analytics visualization tools, can be applied not just to big data but to small data as well. This paper illustrates how some of these tools can be used by focusing on a short first-person narrative. And the NLP tools reveal patterns of language use perhaps not immediately discernible, thus proving useful in the analysis of even small data. But understanding and interpreting these patterns requires knowledge way beyond the NLP tools themselves. Humanists and social scientists need not fear computer scientists; rather, they need to learn to take advantage of them. NLP tools lay a bridge between quality and quantity, with much to be gained from a constant interaction between distant and close reading.",
		"container-title": "Quality & Quantity",
		"DOI": "10.1007/s11135-020-01067-6",
		"ISSN": "1573-7845",
		"journalAbbreviation": "Qual Quant",
		"language": "en",
		"source": "Springer Link",
		"title": "What’s in a text? Bridging the gap between quality and quantity in the digital era",
		"title-short": "What’s in a text?",
		"URL": "https://doi.org/10.1007/s11135-020-01067-6",
		"author": [
			{
				"family": "Franzosi",
				"given": "Roberto"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					1,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020",
					11,
					11
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/897DPHEI",
		"type": "book",
		"call-number": "P96.N35 D38 2018",
		"collection-title": "A K Peters Visualization Series",
		"event-place": "Boca Raton, Florida",
		"ISBN": "978-1-138-19710-7",
		"number-of-pages": "296",
		"publisher": "CRC Press/Taylor & Francis Group",
		"publisher-place": "Boca Raton, Florida",
		"source": "Library of Congress ISBN",
		"title": "Data-driven storytelling",
		"editor": [
			{
				"family": "Riche",
				"given": "Nathalie Henry"
			},
			{
				"family": "Hurter",
				"given": "Christophe"
			},
			{
				"family": "Diakopoulos",
				"given": "Nicholas"
			},
			{
				"family": "Carpendale",
				"given": "Sheelagh"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/KFC2G9VQ",
		"type": "book",
		"edition": "Expanded 2. ed",
		"event-place": "London",
		"ISBN": "978-1-86189-388-8",
		"language": "eng",
		"note": "OCLC: 836906404",
		"number-of-pages": "248",
		"publisher": "Reaktion Books",
		"publisher-place": "London",
		"source": "Gemeinsamer Bibliotheksverbund ISBN",
		"title": "Digital culture",
		"author": [
			{
				"family": "Gere",
				"given": "Charlie"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2008"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6FC8MCCL",
		"type": "book",
		"event-place": "London",
		"ISBN": "978-0-340-64525-3",
		"language": "eng",
		"note": "OCLC: 636777725",
		"number-of-pages": "243",
		"publisher": "Hodder & Stoughton",
		"publisher-place": "London",
		"source": "Gemeinsamer Bibliotheksverbund ISBN",
		"title": "Being digital",
		"author": [
			{
				"family": "Negroponte",
				"given": "Nicholas"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1995"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/NGAJFMZ6",
		"type": "book",
		"event-place": "Madrid",
		"ISBN": "978-84-15832-10-2",
		"language": "English",
		"note": "OCLC: 892201485",
		"publisher": "Turner",
		"publisher-place": "Madrid",
		"source": "Open WorldCat",
		"title": "Big data: la revolución de los datos masivos",
		"title-short": "Big data",
		"author": [
			{
				"family": "Mayer-Schönberger",
				"given": "Viktor"
			},
			{
				"family": "Cukier",
				"given": "Kenneth"
			},
			{
				"family": "Iriarte",
				"given": "Antonio"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VIV3PC5W",
		"type": "article-journal",
		"container-title": "Internet Policy Review",
		"DOI": "10.14763/2019.4.1428",
		"ISSN": "2197-6775",
		"issue": "4",
		"language": "en",
		"source": "DOI.org (Crossref)",
		"title": "Datafication",
		"URL": "https://policyreview.info/concepts/datafication",
		"volume": "8",
		"author": [
			{
				"family": "Mejias",
				"given": "Ulises A."
			},
			{
				"family": "Couldry",
				"given": "Nick"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					2,
					11
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2019",
					11,
					29
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JR97YKXH",
		"type": "article-journal",
		"container-title": "Canadian Historical Review",
		"DOI": "10.3138/chr-2020-0023",
		"ISSN": "0008-3755, 1710-1093",
		"issue": "4",
		"journalAbbreviation": "Canadian Historical Review",
		"language": "en",
		"page": "602-621",
		"source": "DOI.org (Crossref)",
		"title": "We Are All Digital Now: Digital Photography and the Reshaping of Historical Practice",
		"title-short": "We Are All Digital Now",
		"URL": "https://utpjournals.press/doi/10.3138/chr-2020-0023",
		"volume": "101",
		"author": [
			{
				"family": "Milligan",
				"given": "Ian"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					2,
					11
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020",
					12
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ZHEUKZ7I",
		"type": "book",
		"collection-number": "economía, sociedad y cultura / Manuel Castells ; Vol. 1",
		"collection-title": "La era de la información",
		"edition": "3. ed",
		"event-place": "Madrid",
		"ISBN": "978-84-206-7700-2",
		"language": "spa",
		"note": "OCLC: 838044803",
		"number-of-pages": "645",
		"publisher": "Alianza Ed",
		"publisher-place": "Madrid",
		"source": "Gemeinsamer Bibliotheksverbund ISBN",
		"title": "La sociedad red",
		"author": [
			{
				"family": "Castells",
				"given": "Manuel"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2005"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QGGI5RGA",
		"type": "chapter",
		"call-number": "AZ105 .D44 2013",
		"container-title": "Defining digital humanities: a reader",
		"event-place": "Farnham, Surrey, England : Burlington, VT",
		"ISBN": "978-1-4094-6962-9",
		"page": "1-10",
		"publisher": "Ashgate Publishing Limited ; Ashgate Publishing Company",
		"publisher-place": "Farnham, Surrey, England : Burlington, VT",
		"source": "Library of Congress ISBN",
		"title": "Introduction",
		"URL": "PDF/terras1.pdf",
		"editor": [
			{
				"family": "Terras",
				"given": "Melissa M."
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"author": [
			{
				"family": "Terras",
				"given": "Melissa M."
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/STYF8EQE",
		"type": "chapter",
		"call-number": "AZ105 .D44 2013",
		"container-title": "Defining digital humanities: a reader",
		"event-place": "Farnham, Surrey, England : Burlington, VT",
		"ISBN": "978-1-4094-6962-9",
		"page": "279-287",
		"publisher": "Ashgate Publishing Limited ; Ashgate Publishing Company",
		"publisher-place": "Farnham, Surrey, England : Burlington, VT",
		"source": "Library of Congress ISBN",
		"title": "Selected Definitions from the Day of Digital Humanities: 2009-2012",
		"URL": "PDF/terras.pdf",
		"editor": [
			{
				"family": "Terras",
				"given": "Melissa M."
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/W2FECU4M",
		"type": "chapter",
		"call-number": "AZ105 .D44 2013",
		"container-title": "Defining digital humanities: a reader",
		"event-place": "Farnham, Surrey, England : Burlington, VT",
		"ISBN": "978-1-4094-6962-9",
		"page": "289-297",
		"publisher": "Ashgate Publishing Limited ; Ashgate Publishing Company",
		"publisher-place": "Farnham, Surrey, England : Burlington, VT",
		"source": "Library of Congress ISBN",
		"title": "Digital Humanities Definitions by Type",
		"URL": "PDF/gibbs.psf",
		"editor": [
			{
				"family": "Terras",
				"given": "Melissa M."
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"author": [
			{
				"family": "Gibbs",
				"given": "Fred"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JMBJIEK5",
		"type": "chapter",
		"container-title": "Humanidades digitales: una mirada desde la interdisceplinariedad",
		"event-place": "Berlin ; New York",
		"ISBN": "978-3-631-78977-3",
		"page": "7-36",
		"publisher": "Peter Lang",
		"publisher-place": "Berlin ; New York",
		"source": "Library of Congress ISBN",
		"title": "El vértigo de las humanidades digitales ante lo digital: hacia un nuevo paradigma",
		"URL": "PDF/blasco.pdf",
		"editor": [
			{
				"family": "Álvarez Ramos",
				"given": "Eva"
			}
		],
		"author": [
			{
				"family": "Blasco",
				"given": "Javier"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/TKF3IK4J",
		"type": "book",
		"abstract": "\"Data and its technologies now play a large and growing role in humanities research and teaching. This book addresses the needs of humanities scholars who seek deeper expertise in the area of data modeling and representation. The authors, all experts in digital humanities, offer a clear explanation of key technical principles, a grounded discussion of case studies, and an exploration of important theoretical concerns. The book opens with an orientation, giving the reader a history of data modeling in the humanities and a grounding in the technical concepts necessary to understand and engage with the second part of the book. The second part of the book is a wide-ranging exploration of topics central for a deeper understanding of data modeling in digital humanities. Chapters cover data modeling standards and the role they play in shaping digital humanities practice, traditional forms of modeling in the humanities and how they have been transformed by digital approaches, ontologies which seek to anchor meaning in digital humanities resources, and how data models inhabit the other analytical tools used in digital humanities research. It concludes with a glossary chapter that explains specific terms and concepts for data modeling in the digital humanities context. This book is a unique and invaluable resource for teaching and practising data modeling in a digital humanities context\"--",
		"call-number": "AZ105 .S43 2019",
		"collection-title": "Digital research in the arts and humanities",
		"event-place": "London ; New York",
		"ISBN": "978-1-4724-4324-3",
		"number-of-pages": "341",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London ; New York",
		"source": "Library of Congress ISBN",
		"title": "The shape of data in the digital humanities: modeling texts and text-based resources",
		"title-short": "The shape of data in the digital humanities",
		"editor": [
			{
				"family": "Flanders",
				"given": "Julia"
			},
			{
				"family": "Jannidis",
				"given": "Fotis"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/KMDUY4N9",
		"type": "chapter",
		"abstract": "\"Data and its technologies now play a large and growing role in humanities research and teaching. This book addresses the needs of humanities scholars who seek deeper expertise in the area of data modeling and representation. The authors, all experts in digital humanities, offer a clear explanation of key technical principles, a grounded discussion of case studies, and an exploration of important theoretical concerns. The book opens with an orientation, giving the reader a history of data modeling in the humanities and a grounding in the technical concepts necessary to understand and engage with the second part of the book. The second part of the book is a wide-ranging exploration of topics central for a deeper understanding of data modeling in digital humanities. Chapters cover data modeling standards and the role they play in shaping digital humanities practice, traditional forms of modeling in the humanities and how they have been transformed by digital approaches, ontologies which seek to anchor meaning in digital humanities resources, and how data models inhabit the other analytical tools used in digital humanities research. It concludes with a glossary chapter that explains specific terms and concepts for data modeling in the digital humanities context. This book is a unique and invaluable resource for teaching and practising data modeling in a digital humanities context\"--",
		"call-number": "AZ105 .S43 2019",
		"collection-title": "Digital research in the arts and humanities",
		"container-title": "The shape of data in the digital humanities: modeling texts and text-based resources",
		"event-place": "London ; New York",
		"ISBN": "978-1-4724-4324-3",
		"page": "26-95",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London ; New York",
		"source": "Library of Congress ISBN",
		"title": "A gentle introduction to data modeling",
		"editor": [
			{
				"family": "Flanders",
				"given": "Julia"
			},
			{
				"family": "Jannidis",
				"given": "Fotis"
			}
		],
		"author": [
			{
				"family": "Jannidis",
				"given": "Fotis"
			},
			{
				"family": "Flanders",
				"given": "Julia"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/J9Y567U7",
		"type": "article-journal",
		"container-title": "Journal of Digital Humanities",
		"issue": "3",
		"language": "en-US",
		"title": "Big? Smart? Clean? Messy? Data in the Humanities",
		"title-short": "Big? Smart? Clean? Messy?",
		"URL": "http://journalofdigitalhumanities.org/2-3/big-smart-clean-messy-data-in-the-humanities/",
		"volume": "2",
		"author": [
			{
				"family": "Schöch",
				"given": "Christof"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					3,
					15
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6WXWGH93",
		"type": "article-journal",
		"abstract": "The advent of digital resources, the Internet, and an interconnected globe has deeply affected the humanities and its research. Music scholars in Latin America, like everywhere else, have observed this explosion of digital information sharing, but not everyone has been able to take advantage of the new opportunities afforded by this technology. On the one hand, advantages of digitization are slowly becoming recognized as tools to fight the enormous size of the region (Latin America), especially through technology's ability to easily and promptly disperse sources across great distances. In addition, digitization acts as an aid in countering the endemic lack of economic resources, and more broadly offers a path towards making the academic world a more connected and equal place. On the other hand, it is undeniable that the digital revolution has not reached people across the globe equally. Digital segregation is a problem that deeply impacts numerous nations around world; and for Latin America and the Caribbean, it has meant a slower pace of incorporation into the digital era. Key databases like JSTOR and the various READEX products are still largely unavailable to scholars in Latin America, and, given the steep price of such resources, the fight for a world of open-source information is becoming increasingly political.",
		"container-title": "Nineteenth-Century Music Review",
		"DOI": "10.1017/S1479409819000703",
		"ISSN": "1479-4098, 2044-8414",
		"issue": "1",
		"language": "en",
		"note": "publisher: Cambridge University Press",
		"page": "121-127",
		"source": "Cambridge University Press",
		"title": "Digital Humanities and Nineteenth Century Music: Some Perspectives and Examples from Latin America",
		"title-short": "Digital Humanities and Nineteenth Century Music",
		"URL": "https://www.cambridge.org/core/journals/nineteenth-century-music-review/article/abs/digital-humanities-and-nineteenth-century-music-some-perspectives-and-examples-from-latin-america/D7B3338AA6A0BD167E6C5D46A08AF66C",
		"volume": "18",
		"author": [
			{
				"family": "Izquierdo",
				"given": "José Manuel"
			},
			{
				"family": "Vera",
				"given": "Fernanda"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					6,
					2
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2021",
					4
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7VIHDB3M",
		"type": "book",
		"event-place": "Santa Barbara",
		"ISBN": "978-1-953035-57-8",
		"publisher": "Punctum Books",
		"publisher-place": "Santa Barbara",
		"source": "Library of Congress ISBN",
		"title": "Alternative historiographies of the digital humanities",
		"editor": [
			{
				"family": "Kim",
				"given": "Dorothy"
			},
			{
				"family": "Koh",
				"given": "Adeline"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/M5GNPKQU",
		"type": "article-journal",
		"abstract": "The increasing integration of technology into our lives has created unprecedented volumes of data on society’s everyday behaviour. Such data opens up exciting new opportunities to work towards a quantitative understanding of our complex social systems, within the realms of a new discipline known as Computational Social Science. Against a background of financial crises, riots and international epidemics, the urgent need for a greater comprehension of the complexity of our interconnected global society and an ability to apply such insights in policy decisions is clear. This manifesto outlines the objectives of this new scientific direction, considering the challenges involved in it, and the extensive impact on science, technology and society that the success of this endeavour is likely to bring about.",
		"container-title": "The European Physical Journal Special Topics",
		"DOI": "10.1140/epjst/e2012-01697-8",
		"ISSN": "1951-6401",
		"issue": "1",
		"journalAbbreviation": "Eur. Phys. J. Spec. Top.",
		"language": "en",
		"page": "325-346",
		"source": "Springer Link",
		"title": "Manifesto of computational social science",
		"URL": "https://doi.org/10.1140/epjst/e2012-01697-8",
		"volume": "214",
		"author": [
			{
				"family": "Conte",
				"given": "R."
			},
			{
				"family": "Gilbert",
				"given": "N."
			},
			{
				"family": "Bonelli",
				"given": "G."
			},
			{
				"family": "Cioffi-Revilla",
				"given": "C."
			},
			{
				"family": "Deffuant",
				"given": "G."
			},
			{
				"family": "Kertesz",
				"given": "J."
			},
			{
				"family": "Loreto",
				"given": "V."
			},
			{
				"family": "Moat",
				"given": "S."
			},
			{
				"family": "Nadal",
				"given": "J. -P."
			},
			{
				"family": "Sanchez",
				"given": "A."
			},
			{
				"family": "Nowak",
				"given": "A."
			},
			{
				"family": "Flache",
				"given": "A."
			},
			{
				"family": "San Miguel",
				"given": "M."
			},
			{
				"family": "Helbing",
				"given": "D."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					8,
					5
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2012",
					11,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/3RJ483WD",
		"type": "chapter",
		"container-title": "Terra Incognita: Libro blanco sobre transdisciplinariedad y nuevas formas de investigación en el Sistema Español de Ciencia y Tecnología",
		"event-place": "Burgos",
		"ISBN": "978-84-09-23333-5",
		"language": "es",
		"note": "Book Title: Terra Incognita: Libro blanco sobre transdisciplinariedad y nuevas formas de investigación en el Sistema Español de Ciencia y Tecnología\npublisher: Pressbooks",
		"publisher": "Pressbooks",
		"publisher-place": "Burgos",
		"source": "terraincognita.pressbooks.com",
		"title": "Ciencias Sociales Computacionales y Humanidades Digitales: un ejemplo de praxis transdisciplinar",
		"title-short": "Ciencias Sociales Computacionales y Humanidades Digitales",
		"URL": "https://terraincognita.pressbooks.com/chapter/ciencias-sociales-computacionales-y-humanidades-digitales-un-ejemplo-de-praxis-transdisciplinar/",
		"author": [
			{
				"family": "Caro",
				"given": "Jorge"
			},
			{
				"family": "Fuente",
				"given": "Silvia Díaz-de",
				"dropping-particle": "la"
			},
			{
				"family": "Ahedo",
				"given": "Virginia"
			},
			{
				"family": "Zurro",
				"given": "Débora"
			},
			{
				"family": "Madella",
				"given": "Marco"
			},
			{
				"family": "Galán",
				"given": "José Manuel"
			},
			{
				"family": "Izquierdo",
				"given": "Luis R."
			},
			{
				"family": "Santos",
				"given": "José Ignacio"
			},
			{
				"family": "Olmo",
				"given": "Ricardo",
				"dropping-particle": "del"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					8,
					5
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/MQGLSYRS",
		"type": "book",
		"call-number": "HM626",
		"collection-number": "45",
		"collection-title": "Routledge studies in new media and cyberculture",
		"event-place": "New York",
		"ISBN": "978-0-429-49230-3",
		"language": "en",
		"publisher": "Routledge",
		"publisher-place": "New York",
		"source": "Library of Congress ISBN",
		"title": "The discursive power of memes in digital culture: ideology, semiotics, and intertextuality",
		"title-short": "The discursive power of memes in digital culture",
		"author": [
			{
				"family": "Wiggins",
				"given": "Bradley E."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5JWQJE8C",
		"type": "book",
		"collection-title": "Digital humanities / Global computing",
		"edition": "First published",
		"event-place": "Brooklyn, NY",
		"ISBN": "978-0-692-58044-8",
		"language": "eng",
		"number-of-pages": "254",
		"publisher": "punctum books",
		"publisher-place": "Brooklyn, NY",
		"source": "K10plus ISBN",
		"title": "The digital humanist: a critical inquiry",
		"title-short": "The digital humanist",
		"author": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Numerico",
				"given": "Teresa"
			},
			{
				"family": "Tomasi",
				"given": "Francesca"
			}
		],
		"translator": [
			{
				"family": "Schmidt",
				"given": "Desmond"
			},
			{
				"family": "Ferguson",
				"given": "Christopher"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/UCWP4G9C",
		"type": "chapter",
		"collection-title": "Digital humanities / Global computing",
		"container-title": "The digital humanist: a critical inquiry",
		"edition": "First published",
		"event-place": "Brooklyn, NY",
		"ISBN": "978-0-692-58044-8",
		"language": "eng",
		"page": "207-218",
		"publisher": "punctum books",
		"publisher-place": "Brooklyn, NY",
		"source": "K10plus ISBN",
		"title": "DH in a global perspective",
		"author": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Numerico",
				"given": "Teresa"
			},
			{
				"family": "Tomasi",
				"given": "Francesca"
			}
		],
		"translator": [
			{
				"family": "Schmidt",
				"given": "Desmond"
			},
			{
				"family": "Ferguson",
				"given": "Christopher"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/TEHX2YQE",
		"type": "book",
		"abstract": "\"As digital media, tools, and techniques continue to impact and advance the humanities, Doing More Digital Humanities provides practical information on how to do digital humanities work. This book offers: A comprehensive, practical guide to the digital humanities ; Accessible introductions, which in turn provide the grounding for the more advanced chapters within the book ; An overview of core competencies, to help research teams, administrators, and allied groups, make informed decisions about suitable collaborators, skills development, and workflow ; Guidance for individuals, collaborative teams, and academic managers who support digital humanities researchers ; Contextualized case studies, including examples of projects, tools, centres, labs, and research clusters ; Resources for starting digital humanities projects, including links to further readings, training materials and exercises, and resources beyond ; Additional augmented content that complements the guidance and case studies in Doing Digital Humanities\"--",
		"call-number": "AZ105 .D595 2020",
		"event-place": "London ; New York, NY",
		"ISBN": "978-0-367-19270-9",
		"number-of-pages": "333",
		"publisher": "Routledge/Taylor & Francis Group",
		"publisher-place": "London ; New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Doing more digital humanities: open approaches to creation, growth, and development",
		"title-short": "Doing more digital humanities",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/XJUMGYKD",
		"type": "chapter",
		"abstract": "\"As digital media, tools, and techniques continue to impact and advance the humanities, Doing More Digital Humanities provides practical information on how to do digital humanities work. This book offers: A comprehensive, practical guide to the digital humanities ; Accessible introductions, which in turn provide the grounding for the more advanced chapters within the book ; An overview of core competencies, to help research teams, administrators, and allied groups, make informed decisions about suitable collaborators, skills development, and workflow ; Guidance for individuals, collaborative teams, and academic managers who support digital humanities researchers ; Contextualized case studies, including examples of projects, tools, centres, labs, and research clusters ; Resources for starting digital humanities projects, including links to further readings, training materials and exercises, and resources beyond ; Additional augmented content that complements the guidance and case studies in Doing Digital Humanities\"--",
		"call-number": "AZ105 .D595 2020",
		"container-title": "Doing more digital humanities: open approaches to creation, growth, and development",
		"event-place": "London ; New York, NY",
		"ISBN": "978-0-367-19270-9",
		"page": "25-37",
		"publisher": "Routledge/Taylor & Francis Group",
		"publisher-place": "London ; New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Getting started. Strategies for DH professional development",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "Morgan",
				"given": "Paige"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/X34YNAC4",
		"type": "book",
		"call-number": "AZ105 .B44 2015",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-02868-4",
		"number-of-pages": "574",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "Between humanities and the digital",
		"editor": [
			{
				"family": "Svensson",
				"given": "Patrik"
			},
			{
				"family": "Goldberg",
				"given": "David Theo"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QM7BYI3J",
		"type": "chapter",
		"call-number": "AZ105 .B44 2015",
		"container-title": "Between humanities and the digital",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-02868-4",
		"language": "en",
		"page": "391-400",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "The Humanitoscope - Exploring the situatedness of Humanities Infrastructure",
		"editor": [
			{
				"family": "Svensson",
				"given": "Patrik"
			},
			{
				"family": "Goldberg",
				"given": "David Theo"
			}
		],
		"author": [
			{
				"family": "Svensson",
				"given": "Patrick"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/SU2LX9AB",
		"type": "book",
		"call-number": "AZ105 .A35 2014",
		"edition": "1st edition",
		"event-place": "New York, NY",
		"ISBN": "978-1-138-89943-8",
		"publisher": "Routledge",
		"publisher-place": "New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Doing digital humanities: practice, training, research",
		"title-short": "Doing digital humanities",
		"author": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/FVYF9F85",
		"type": "chapter",
		"call-number": "AZ105 .A35 2014",
		"container-title": "Doing digital humanities: practice, training, research",
		"edition": "1st edition",
		"event-place": "New York, NY",
		"ISBN": "978-1-138-89943-8",
		"language": "en",
		"page": "22-34",
		"publisher": "Routledge",
		"publisher-place": "New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Global outlooks in digital humanities. Multilingual practices and minimal computing",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "Gil",
				"given": "Alex"
			},
			{
				"family": "Ortega",
				"given": "Élika"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7KSI7WZ3",
		"type": "chapter",
		"call-number": "AZ105 .B44 2015",
		"container-title": "Between humanities and the digital",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-02868-4",
		"language": "en",
		"page": "391-400",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "The Digital Humanities as a Laboratory",
		"editor": [
			{
				"family": "Svensson",
				"given": "Patrik"
			},
			{
				"family": "Goldberg",
				"given": "David Theo"
			}
		],
		"author": [
			{
				"family": "Earhart",
				"given": "Amy E."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/2XLF6MUL",
		"type": "book",
		"call-number": "AZ105 .C85 2018",
		"event-place": "London : New York",
		"ISBN": "978-1-4724-4712-8",
		"number-of-pages": "172",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London : New York",
		"source": "Library of Congress ISBN",
		"title": "Cultural heritage infrastructures in digital humanities",
		"editor": [
			{
				"family": "Benardou",
				"given": "Agiatis"
			},
			{
				"family": "Champion",
				"given": "Erik"
			},
			{
				"family": "Dallas",
				"given": "Costis"
			},
			{
				"family": "Hughes",
				"given": "Lorna M."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/M94XGK97",
		"type": "chapter",
		"call-number": "AZ105 .C85 2018",
		"container-title": "Cultural heritage infrastructures in digital humanities",
		"event-place": "London : New York",
		"ISBN": "978-1-4724-4712-8",
		"language": "en",
		"page": "1-14",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London : New York",
		"source": "Library of Congress ISBN",
		"title": "Introduction: a critique of digital practices and research infrastructures",
		"editor": [
			{
				"family": "Benardou",
				"given": "Agiatis"
			},
			{
				"family": "Champion",
				"given": "Erik"
			},
			{
				"family": "Dallas",
				"given": "Costis"
			},
			{
				"family": "Hughes",
				"given": "Lorna M."
			}
		],
		"author": [
			{
				"family": "Benardou",
				"given": "Agiatis"
			},
			{
				"family": "Champion",
				"given": "Erik"
			},
			{
				"family": "Dallas",
				"given": "Costis"
			},
			{
				"family": "Hughes",
				"given": "Lorna M."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QK8HM953",
		"type": "book",
		"event-place": "Ciudad de México",
		"ISBN": "978-607-8560-59-2",
		"language": "Spanish",
		"note": "OCLC: 1098731766",
		"publisher": "Bonilla Artigas",
		"publisher-place": "Ciudad de México",
		"source": "Open WorldCat",
		"title": "Humanidades digitales: recepción, institucionalización y crítica",
		"editor": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			},
			{
				"family": "Barrón Tovar",
				"given": "José Francisco"
			},
			{
				"literal": "Encuentro de Humanistas Digitales"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/C8MGNB6B",
		"type": "chapter",
		"container-title": "Humanidades digitales: recepción, institucionalización y crítica",
		"event-place": "Ciudad de México",
		"ISBN": "978-607-8560-59-2",
		"language": "Spanish",
		"note": "OCLC: 1098731766",
		"page": "17-37",
		"publisher": "Bonilla Artigas",
		"publisher-place": "Ciudad de México",
		"source": "Open WorldCat",
		"title": "La institucionalización de las humanidades digitales",
		"editor": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			},
			{
				"family": "Barrón Tovar",
				"given": "José Francisco"
			},
			{
				"literal": "Encuentro de Humanistas Digitales"
			}
		],
		"author": [
			{
				"family": "Galina Russell, Isabel",
				"given": ""
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Y7BNSYTU",
		"type": "chapter",
		"abstract": "\"As digital media, tools, and techniques continue to impact and advance the humanities, Doing More Digital Humanities provides practical information on how to do digital humanities work. This book offers: A comprehensive, practical guide to the digital humanities ; Accessible introductions, which in turn provide the grounding for the more advanced chapters within the book ; An overview of core competencies, to help research teams, administrators, and allied groups, make informed decisions about suitable collaborators, skills development, and workflow ; Guidance for individuals, collaborative teams, and academic managers who support digital humanities researchers ; Contextualized case studies, including examples of projects, tools, centres, labs, and research clusters ; Resources for starting digital humanities projects, including links to further readings, training materials and exercises, and resources beyond ; Additional augmented content that complements the guidance and case studies in Doing Digital Humanities\"--",
		"call-number": "AZ105 .D595 2020",
		"container-title": "Doing more digital humanities: open approaches to creation, growth, and development",
		"event-place": "London ; New York, NY",
		"ISBN": "978-0-367-19270-9",
		"page": "7-24",
		"publisher": "Routledge/Taylor & Francis Group",
		"publisher-place": "London ; New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Legacy technologies and digital futures",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "Estill",
				"given": "Laura"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/EZBD7ZTD",
		"type": "chapter",
		"abstract": "\"As digital media, tools, and techniques continue to impact and advance the humanities, Doing More Digital Humanities provides practical information on how to do digital humanities work. This book offers: A comprehensive, practical guide to the digital humanities ; Accessible introductions, which in turn provide the grounding for the more advanced chapters within the book ; An overview of core competencies, to help research teams, administrators, and allied groups, make informed decisions about suitable collaborators, skills development, and workflow ; Guidance for individuals, collaborative teams, and academic managers who support digital humanities researchers ; Contextualized case studies, including examples of projects, tools, centres, labs, and research clusters ; Resources for starting digital humanities projects, including links to further readings, training materials and exercises, and resources beyond ; Additional augmented content that complements the guidance and case studies in Doing Digital Humanities\"--",
		"call-number": "AZ105 .D595 2020",
		"container-title": "Doing more digital humanities: open approaches to creation, growth, and development",
		"event-place": "London ; New York, NY",
		"ISBN": "978-0-367-19270-9",
		"page": "38-57",
		"publisher": "Routledge/Taylor & Francis Group",
		"publisher-place": "London ; New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Negotiating sustainability. Building digital humanities projects that last",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "Goddard",
				"given": "Lisa"
			},
			{
				"family": "Seeman",
				"given": "Dean"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JNHI2FCS",
		"type": "chapter",
		"container-title": "Humanidades Digitais e o mundo lusófono",
		"event-place": "Rio de Janeiro",
		"ISBN": "978-65-5652-070-4",
		"language": "pr",
		"page": "8-11",
		"publisher": "FGV",
		"publisher-place": "Rio de Janeiro",
		"title": "Humanidades Digitais e o mundo lusófono. Prefacio para las “otras” Humanidades Digitales",
		"title-short": "Humanidades Digitais e o mundo lusófono",
		"author": [
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"editor": [
			{
				"family": "Pimenta",
				"given": "Ricardo M."
			},
			{
				"family": "Alves",
				"given": "Daniel"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/NFJ3GZE3",
		"type": "chapter",
		"container-title": "Digital humanities and scholarly research trends in the Asia-Pacific",
		"page": "1-18",
		"publisher": "IGI Global",
		"title": "Tracing the Development of Digital Humanities in Australia",
		"author": [
			{
				"family": "Arthur",
				"given": "Paul Longley"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/98XLBP34",
		"type": "chapter",
		"call-number": "AZ105 .B44 2015",
		"container-title": "Between humanities and the digital",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-02868-4",
		"language": "en",
		"page": "95-107",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "Beyond Infrastructure: Re-humanizing Digital Humanities in India",
		"editor": [
			{
				"family": "Svensson",
				"given": "Patrik"
			},
			{
				"family": "Goldberg",
				"given": "David Theo"
			}
		],
		"author": [
			{
				"family": "Shah",
				"given": "Nishant"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WGBFE5E7",
		"type": "book",
		"event-place": "México",
		"ISBN": "978-84-17341-10-7",
		"language": "Spanish",
		"note": "OCLC: 1117760787",
		"publisher": "Gedisa",
		"publisher-place": "México",
		"source": "Open WorldCat",
		"title": "Humanidades digitales: la cultura frente a las nuevas tecnologías",
		"title-short": "Humanidades digitales",
		"author": [
			{
				"family": "Vinck",
				"given": "Dominique"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ARUZP859",
		"type": "chapter",
		"container-title": "Humanidades digitales: la cultura frente a las nuevas tecnologías",
		"event-place": "México",
		"ISBN": "978-84-17341-10-7",
		"language": "Spanish",
		"note": "OCLC: 1117760787",
		"page": "117-139",
		"publisher": "Gedisa",
		"publisher-place": "México",
		"source": "Open WorldCat",
		"title": "Las humanidades digitales en el mundo",
		"author": [
			{
				"family": "Vinck",
				"given": "Dominique"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/V76XXRFL",
		"type": "book",
		"call-number": "P90 .R673 2018",
		"event-place": "New York",
		"ISBN": "978-1-138-84430-8",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "New York",
		"source": "Library of Congress ISBN",
		"title": "The Routledge companion to media studies and digital humanities",
		"editor": [
			{
				"family": "Sayers",
				"given": "Jentery"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Z49TAP2V",
		"type": "chapter",
		"call-number": "P90 .R673 2018",
		"container-title": "The Routledge companion to media studies and digital humanities",
		"event-place": "New York",
		"ISBN": "978-1-138-84430-8",
		"language": "en",
		"page": "78-86",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "New York",
		"source": "Library of Congress ISBN",
		"title": "Decolonizing the Digital Humanities in Theory and Practice",
		"title-short": "Decolonizing the Digital Humanities",
		"editor": [
			{
				"family": "Sayers",
				"given": "Jentery"
			}
		],
		"author": [
			{
				"family": "Risam",
				"given": "Roopika"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/HJG7X3M9",
		"type": "article-journal",
		"abstract": "Tanto para las Digital Humanities como para las Humanidades Digitales, el core de la investigación son los proyectos que se expresan a través de repositorios y bases de datos, ediciones digitales académicas, blogs, o bibliotecas digitales disponibles, en su amplísima mayoría, de forma gratuita y online. La investigación abierta parece haber nacido con las Digital Humanities, aunque poco se haya hablado hasta ahora de ella.   Una evaluación adecuada y equitativa de la investigación científica en Humanidades Digitales colaborará con la construcción del campo científico y el nuevo paradigma del conocimiento en la que estas se imbrican, como la de la investigación o ciencia abierta.",
		"container-title": "Exlibris",
		"ISSN": "2314-3894",
		"issue": "7",
		"language": "es",
		"license": "Los autores que publiquen en esta revista aceptan las siguientes condiciones: 1) los autores conservan los derechos de autor y ceden a la revista el derecho de la primera publicación, con el trabajo registrado con  Licencia Creative Commons Atribución 4.0 Internacional , que permite a terceros utilizar lo publicado siempre que mencionen la autoría del trabajo y la primera publicación en esta revista; 2) los autores pueden realizar otros acuerdos contractuales independientes y adicionales para la distribución no exclusiva de la versión del artículo publicado en esta revista (p. ej., incluirlo en un repositorio institucional o publicarlo en un libro) siempre que indiquen claramente que el trabajo se publicó por primera vez en esta revista; 3) se permite y recomienda a los autores a publicar su trabajo en Internet (por ejemplo en páginas institucionales o personales).",
		"note": "number: 7",
		"page": "136-149",
		"source": "revistas.filo.uba.ar",
		"title": "Humanidades digitales bajo la lupa: investigación abierta y evaluación científica",
		"title-short": "Humanidades digitales bajo la lupa",
		"URL": "http://revistas.filo.uba.ar/index.php/exlibris/article/view/3177",
		"volume": "0",
		"author": [
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					8,
					10
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/HRRFPM3Y",
		"type": "article-journal",
		"abstract": "Autorías: Juan Manuel Lacalle, Mariano Vilar.\nLocalización: Anclajes. Nº. 1, 2019.\nArtículo de Revista en Dialnet.",
		"container-title": "Anclajes",
		"DOI": "10/gjg9vc",
		"ISSN": "1851-4669",
		"issue": "1 (enero-abril)",
		"language": "spa",
		"note": "ZSCC: 0000001 \nPropuesto por Silvia Gutiérrez @espejolento",
		"page": "19-40",
		"source": "dialnet.unirioja.es",
		"title": "Estudios literarios y lectura distante: un primer acercamiento a la actualidad de la investigación en las revistas académicas argentinas",
		"title-short": "Estudios literarios y lectura distante",
		"URL": "https://dialnet.unirioja.es/servlet/articulo?codigo=6727952",
		"volume": "23",
		"author": [
			{
				"family": "Lacalle",
				"given": "Juan Manuel"
			},
			{
				"family": "Vilar",
				"given": "Mariano"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2021",
					2,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BCQIVL5C",
		"type": "book",
		"collection-number": "61",
		"collection-title": "Cuadernos artesanos de comunicación",
		"event-place": "La Laguna, Tenerife",
		"ISBN": "978-84-15698-64-7",
		"language": "es",
		"publisher": "Sociedad Latina de Comunicación Social",
		"publisher-place": "La Laguna, Tenerife",
		"title": "Ciencias Sociales y Humanidades Digitales. Técnicas, herramientas y experiencias de e-Research e investigación en colaboración",
		"title-short": "Ciencias Sociales y Humanidades Digitales",
		"URL": "http://www.cuadernosartesanos.org/2014/cac61.pdf",
		"editor": [
			{
				"family": "Romero Frías",
				"given": "Esteban"
			},
			{
				"family": "Sánchez González",
				"given": "María"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2014"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RVTSIE8A",
		"type": "book",
		"abstract": "\"The Digital Humanities Coursebook provides critical frameworks for the application of Digital Humanities tools and platforms, which have become an integral part of work across a wide range of disciplines. Written by an expert with twenty years of experience in this field, the book is focused on the principles and fundamental concepts for application, rather than on specific tools or platforms. Each chapter contains examples of projects, tools, or platforms that demonstrate these principles in action. The book is structured to complement courses on digital humanities and provides a series of modules, each of which is organized around a set of concerns and topics, thought experiments and questions, as well as specific discussion of the ways in which tools and platforms work. The book covers a wide range of topics and clearly details how to integrate the acquisition of expertise in data, metadata, classification, interface, visualization, network analysis, topic modelling, data mining, mapping, and web presentation with issues in intellectual property, sustainability, privacy, and the ethical use of information. Written in an accessible and engaging manner, The Digital Humanities Coursebook will be a useful guide for anyone teaching or studying a course in the areas of digital humanities, library and information science, English, or computer science. The book will provide a framework for direct engagement with digital humanities and, as such, should be of interest to others working across the humanities too\"--",
		"call-number": "AZ105",
		"edition": "First edition",
		"event-place": "Abingdon, Oxon ; New York",
		"ISBN": "978-1-00-036453-8",
		"number-of-pages": "1",
		"publisher": "Routledge/Taylor & Francis",
		"publisher-place": "Abingdon, Oxon ; New York",
		"source": "Library of Congress ISBN",
		"title": "The digital humanities coursebook: an introduction to digital methods for research and scholarship",
		"title-short": "The digital humanities coursebook",
		"author": [
			{
				"family": "Drucker",
				"given": "Johanna"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/82XU3UYQ",
		"type": "chapter",
		"collection-title": "Blackwell Companions to Literature and Culture",
		"container-title": "Companion to Digital Humanities (Blackwell Companions to Literature and Culture)",
		"edition": "Hardcover",
		"event-place": "Oxford",
		"ISBN": "978-1-4051-0321-3",
		"publisher": "Blackwell Publishing Professional",
		"publisher-place": "Oxford",
		"title": "The History of Humanities Computing",
		"URL": "http://www.digitalhumanities.org/companion/view?docId=blackwell/9781405103213/9781405103213.xml&chunk.id=ss1-2-1&toc.depth=1&toc.id=ss1-2-1&brand=default",
		"editor": [
			{
				"family": "Schreibman",
				"given": "Susan"
			},
			{
				"family": "Siemens",
				"given": "Ray"
			},
			{
				"family": "Unsworth",
				"given": "John"
			}
		],
		"author": [
			{
				"family": "Hockey",
				"given": "Susan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2004",
					12
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/PU62NRE6",
		"type": "book",
		"abstract": "\"Confronting the digital revolution in academia, this book examines the application of new computational techniques and visualisation technologies in the Arts & Humanities. Uniting differing perspectives, leading and emerging scholars discuss the theoretical and practicalchallenges that computation raises for these disciplines\"--Provided by publisher",
		"call-number": "AZ105 .U64 2012",
		"event-place": "Houndmills, Basingstoke, Hampshire ; New York",
		"ISBN": "978-0-230-29265-9",
		"note": "OCLC: ocn701020028",
		"number-of-pages": "318",
		"publisher": "Palgrave Macmillan",
		"publisher-place": "Houndmills, Basingstoke, Hampshire ; New York",
		"source": "Library of Congress ISBN",
		"title": "Understanding digital humanities",
		"editor": [
			{
				"family": "Berry",
				"given": "David M."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/774R9BAZ",
		"type": "chapter",
		"abstract": "\"Confronting the digital revolution in academia, this book examines the application of new computational techniques and visualisation technologies in the Arts & Humanities. Uniting differing perspectives, leading and emerging scholars discuss the theoretical and practicalchallenges that computation raises for these disciplines\"--Provided by publisher",
		"call-number": "AZ105 .U64 2012",
		"container-title": "Understanding digital humanities",
		"event-place": "Houndmills, Basingstoke, Hampshire ; New York",
		"ISBN": "978-0-230-29265-9",
		"note": "OCLC: ocn701020028",
		"page": "1-20",
		"publisher": "Palgrave Macmillan",
		"publisher-place": "Houndmills, Basingstoke, Hampshire ; New York",
		"source": "Library of Congress ISBN",
		"title": "Introduction: Understanding the Digital Humanities",
		"editor": [
			{
				"family": "Berry",
				"given": "David M."
			}
		],
		"author": [
			{
				"family": "Berry",
				"given": "David M."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RGU63R7H",
		"type": "book",
		"collection-number": "16",
		"collection-title": "Ciencia, tecnología y sociedad",
		"event-place": "Rubí (Barcelona)",
		"ISBN": "978-84-7658-808-6",
		"language": "spa",
		"number-of-pages": "230",
		"publisher": "Anthropos",
		"publisher-place": "Rubí (Barcelona)",
		"source": "K10plus ISBN",
		"title": "Cibercultura: informe al Consejo de Europa",
		"title-short": "Cibercultura",
		"author": [
			{
				"family": "Lévy",
				"given": "Pierre"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2007"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Z8VUPBD6",
		"type": "book",
		"call-number": "Q355 .R385 2013",
		"collection-title": "Infrastructures series",
		"event-place": "Cambridge, Massachusetts ; London, England",
		"ISBN": "978-0-262-51828-4",
		"number-of-pages": "182",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts ; London, England",
		"source": "Library of Congress ISBN",
		"title": "\"Raw data\" is an oxymoron",
		"editor": [
			{
				"family": "Gitelman",
				"given": "Lisa"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/4B42RT8P",
		"type": "chapter",
		"call-number": "Q355 .R385 2013",
		"collection-title": "Infrastructures series",
		"container-title": "\"Raw data\" is an oxymoron",
		"event-place": "Cambridge, Massachusetts ; London, England",
		"ISBN": "978-0-262-51828-4",
		"page": "15-40",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts ; London, England",
		"source": "Library of Congress ISBN",
		"title": "Data before the Fact",
		"editor": [
			{
				"family": "Gitelman",
				"given": "Lisa"
			}
		],
		"author": [
			{
				"family": "Rosenberg",
				"given": "Daniel"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BY6QPPGM",
		"type": "chapter",
		"abstract": "\"Data and its technologies now play a large and growing role in humanities research and teaching. This book addresses the needs of humanities scholars who seek deeper expertise in the area of data modeling and representation. The authors, all experts in digital humanities, offer a clear explanation of key technical principles, a grounded discussion of case studies, and an exploration of important theoretical concerns. The book opens with an orientation, giving the reader a history of data modeling in the humanities and a grounding in the technical concepts necessary to understand and engage with the second part of the book. The second part of the book is a wide-ranging exploration of topics central for a deeper understanding of data modeling in digital humanities. Chapters cover data modeling standards and the role they play in shaping digital humanities practice, traditional forms of modeling in the humanities and how they have been transformed by digital approaches, ontologies which seek to anchor meaning in digital humanities resources, and how data models inhabit the other analytical tools used in digital humanities research. It concludes with a glossary chapter that explains specific terms and concepts for data modeling in the digital humanities context. This book is a unique and invaluable resource for teaching and practising data modeling in a digital humanities context\"--",
		"call-number": "AZ105 .S43 2019",
		"collection-title": "Digital research in the arts and humanities",
		"container-title": "The shape of data in the digital humanities: modeling texts and text-based resources",
		"event-place": "London ; New York",
		"ISBN": "978-1-4724-4324-3",
		"page": "178-196",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London ; New York",
		"source": "Library of Congress ISBN",
		"title": "Ontologies and data modeling",
		"editor": [
			{
				"family": "Flanders",
				"given": "Julia"
			},
			{
				"family": "Jannidis",
				"given": "Fotis"
			}
		],
		"author": [
			{
				"family": "Eide",
				"given": "Øyvind"
			},
			{
				"family": "Smith Ore",
				"given": "Christian-Emil"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/T5YDPWGQ",
		"type": "chapter",
		"call-number": "AZ105 .A35 2014",
		"container-title": "Doing digital humanities: practice, training, research",
		"edition": "1st edition",
		"event-place": "New York, NY",
		"ISBN": "978-1-138-89943-8",
		"page": "145-162",
		"publisher": "Routledge",
		"publisher-place": "New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Databases",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "Quamen",
				"given": "Harvey"
			},
			{
				"family": "Bath",
				"given": "Jon"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VIKFJ2UA",
		"type": "chapter",
		"call-number": "AZ105 .A35 2014",
		"container-title": "Doing digital humanities: practice, training, research",
		"edition": "1st edition",
		"event-place": "New York, NY",
		"ISBN": "978-1-138-89943-8",
		"page": "343-357",
		"publisher": "Routledge",
		"publisher-place": "New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Project management and the digital humanist",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "Siemens",
				"given": "Lynne"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/862XQZKD",
		"type": "article-journal",
		"abstract": "This question of disciplinary meaning—which I ask from the viewpoint of the humanities generally—is larger than the question of disciplinary identity now preoccupying “DH” itself, as insiders call it. Having reached a critical mass of participants, publications, conferences, grant competitions, institutionalization (centers, programs, and advertised jobs), and general visibility, the field is vigorously forming an identity. Recent debates about whether the digital humanities are a “big tent” (Jockers and Worthey), “who's in and who's out?” (Ramsay), whether “you have to know how to code [or be a builder]” (Ramsay, “On Building”), the need for “more hack, less yack” (Cecire, “When Digital Humanities”; Koh), and “who you calling untheoretical?” (Bauer) witness a dialectics of inclusion and exclusion not unlike that of past emergent fields. An ethnographer of the field, indeed, might take a page from Claude Lévi-Strauss and chart the current digital humanities as something like a grid of affiliations and differences between neighboring tribes. Exaggerating the differences somewhat, as when a tribe boasts its uniqueness, we can thus say that the digital humanities—much of which affiliates with older humanities disciplines such as literature, history, classics, and the languages; with the remediation of older media such as books and libraries; and ultimately with the value of the old itself (history, archives, the curatorial mission)—are not the tribe of “new media studies,” under the sway of the design, visual, and media arts; Continental theory; cultural criticism; and the avant-garde new. Similarly, despite significant trends toward networked and multimodal work spanning social, visual, aural, and haptic media, much of the digital humanities focuses on documents and texts in a way that distinguishes the field's work from digital research in media studies, communication studies, information studies, and sociology. And the digital humanities are exploring new repertoires of interpretive or expressive “algorithmic criticism” (the “second wave” of the digital humanities proclaimed in “The Digital Humanities Manifesto 2.0” [3]) in a way that makes the field not even its earlier self, “humanities computing,” alleged to have had narrower technical and service-oriented aims. Recently, the digital humanities' limited engagement with identity and social-justice issues has also been seen to be a differentiating trait—for example, by the vibrant #transformDH collective, which worries that the digital humanities (unlike some areas of new media studies) are dominantly not concerned with race, gender, alternative sexualities, or disability.",
		"container-title": "Publications of the Modern Language Association of America",
		"DOI": "10.1632/pmla.2013.128.2.409",
		"ISSN": "0030-8129, 1938-1530",
		"issue": "2",
		"journalAbbreviation": "Publ. Mod. Lang. Assoc. Am.",
		"language": "en",
		"page": "409-423",
		"source": "DOI.org (Crossref)",
		"title": "The Meaning of the Digital Humanities",
		"URL": "https://www.cambridge.org/core/product/identifier/S003081290012262X/type/journal_article",
		"volume": "128",
		"author": [
			{
				"family": "Liu",
				"given": "Alan"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					1,
					27
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/U3R2DYL6",
		"type": "paper-conference",
		"abstract": "The modern university has the potential to turn into a nexus of digital embracement and innovation, thus responding to both strategic planning for higher education and societal demands. Priorities in digitalisation strategies (White Paper ‘Bologna Digital 2020’, Rampelt et al. 2019) for higher education institutions (HEIs) are actively promoted, and their implementation is in progress throughout Europe. However, the embedding of the digitalisation reform at the institutional level is considerably uneven from one country to another, with Eastern European HEIs lagging behind (Conrads et al. 2017). The aim of this position paper is to present and discuss the case of digital humanities (DH) as an incentive for digitalisation strategies at Eastern European universities. We briefly contextualize the configuration of DH initiatives in the region by using the results of the Digital Humanities Survey and propose the case study of Romania, where we investigate the implementation status of such initiatives. We further exemplify the process of developing a DH centre and evaluate the institutional impact of the recently created research centre CODHUS, from the West University of Timişoara, Romania, the second DH centre in the country. The strength of the new centre relies on its capacity to converge cross-disciplinary expertise with digital technologies. The centre intends to develop computational solutions and digital tools for research, course development and assessment. CODHUS is also a digital-competence training centre for teachers and students, with the purpose of bridging the gap between teaching strategies and goals, on one hand, and students’ digital experiences and expectations from HEI, on the other. The study offers a multiple-lens perspective on the integration of digital-intensive research initiatives, such as DH, into the Bologna process. We argue that DH centres can support further HE developments which contribute to building “new learning ecologies” (Galvis 2018) and creating an “education area with digital solutions” (Rampelt 2019).",
		"container-title": "European Higher Education Area: Challenges for a New Decade",
		"DOI": "10.1007/978-3-030-56316-5_34",
		"event-place": "Cham",
		"ISBN": "978-3-030-56316-5",
		"language": "en",
		"page": "545-564",
		"publisher": "Springer International Publishing",
		"publisher-place": "Cham",
		"source": "Springer Link",
		"title": "Digital Humanities as an Incentive for Digitalisation Strategies in Eastern European HEIs: A Case Study of Romania",
		"title-short": "Digital Humanities as an Incentive for Digitalisation Strategies in Eastern European HEIs",
		"author": [
			{
				"family": "Chitez",
				"given": "Mădălina"
			},
			{
				"family": "Rogobete",
				"given": "Roxana"
			},
			{
				"family": "Foitoş",
				"given": "Alexandru"
			}
		],
		"editor": [
			{
				"family": "Curaj",
				"given": "Adrian"
			},
			{
				"family": "Deca",
				"given": "Ligia"
			},
			{
				"family": "Pricopie",
				"given": "Remus"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/NVCZLGSF",
		"type": "document",
		"title": "[001.30285] DH2017-abstracts.pdf"
	},
	{
		"id": "http://zotero.org/users/163570/items/Y9YRFY9W",
		"type": "book",
		"ISBN": "978-1-118-68059-9",
		"language": "en",
		"publisher": "Wiley",
		"source": "Zotero",
		"title": "A New Companion to Digital Humanities",
		"editor": [
			{
				"family": "Schreibman",
				"given": "Susan"
			},
			{
				"family": "Siemens",
				"given": "Ray"
			},
			{
				"family": "Unsworth",
				"given": "John"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QWYDFTXS",
		"type": "chapter",
		"abstract": "\"This collection addresses the lack of perspectives beyond Westernized and Anglophone contexts in the digital humanities. Focused on work that has been underappreciated for linguistic, cultural, or geopolitical reasons, contributors showcase alternative histories that detail the rise of the digital humanities in the Global South and other \"invisible\" contexts and explore the implications of a truly global digital humanities\"--",
		"call-number": "AZ105",
		"collection-title": "Debates in the digital humanities",
		"container-title": "Global debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-1-4529-6710-3",
		"page": "ix-xxxvii",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Introduction",
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/PIYZREFG",
		"type": "book",
		"abstract": "\"The use of quantitative methods in the humanities and related social sciences has increased considerably in recent years, allowing researchers to discover patterns in a vast range of source materials. Despite this growth, there are few resources addressed to students and scholars who wish to take advantage of these powerful tools. Humanities Data Analysis offers the first intermediate-level guide to quantitative data analysis for humanities students and scholars using the Python programming language. This practical textbook, which assumes a basic knowledge of Python, teaches readers the necessary skills for conducting humanities research in the rapidly developing digital environment. The book begins with an overview of the place of data science in the humanities, and proceeds to cover data carpentry: the essential techniques for gathering, cleaning, representing, and transforming textual and tabular data. Then, drawing from real-world, publicly available data sets that cover a variety of scholarly domains, the book delves into detailed case studies. Focusing on textual data analysis, the authors explore such diverse topics as network analysis, genre theory, onomastics, literacy, author attribution, mapping, stylometry, topic modeling, and time series analysis. Exercises and resources for further reading are provided at the end of each chapter. An ideal resource for humanities students and scholars aiming to take their Python skills to the next level, Humanities Data Analysis illustrates the benefits that quantitative methods can bring to complex research questions. Appropriate for advanced undergraduates, graduate students, and scholars with a basic knowledge of Python. Applicable to many humanities disciplines, including history, literature, and sociology. Offers real-world case studies using publicly available data sets. Provides exercises at the end of each chapter for students to test acquired skills. Emphasizes visual storytelling via data visualizations\"--",
		"call-number": "AZ186 .K37 2021",
		"event-place": "Princeton",
		"ISBN": "978-0-691-17236-1",
		"publisher": "Princeton University Press",
		"publisher-place": "Princeton",
		"source": "Library of Congress ISBN",
		"title": "Humanities data analysis: case studies with Python",
		"title-short": "Humanities data analysis",
		"author": [
			{
				"family": "Karsdorp",
				"given": "Folgert"
			},
			{
				"family": "Kestemont",
				"given": "Mike"
			},
			{
				"family": "Riddell",
				"given": "Allen"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/XI63RA83",
		"type": "book",
		"abstract": "\"An illuminating volume of critical essays charting the diverse territory of digital humanities scholarship\"--",
		"call-number": "AZ105 .P43 2021",
		"event-place": "Minneapolis",
		"ISBN": "978-1-5179-1067-9",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "People, practice, power: digital humanities outside the center",
		"title-short": "People, practice, power",
		"editor": [
			{
				"family": "Nieves",
				"given": "Angel David"
			},
			{
				"family": "McGrail",
				"given": "Anne B."
			},
			{
				"family": "Senier",
				"given": "Siobhan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JNZUTGWA",
		"type": "book",
		"abstract": "Interdisciplining Digital Humanities sorts through definitions and patterns of practice over roughly sixty-five years of work, providing an overview for specialists and a general audience alike. It is the only book that tests the widespread claim that Digital Humanities is interdisciplinary. By examining the boundary work of constructing, expanding, and sustaining a new field, it depicts both the ways this new field is being situated within individual domains and dynamic cross-fertilizations that are fostering new relationships across academic boundaries. It also accounts for digital reinvigorations of public humanities in cultural heritage institutions of museums, archives, libraries, and community forums.--",
		"event-place": "Ann Arbor",
		"ISBN": "978-0-472-90013-8",
		"language": "English",
		"note": "OCLC: 1105437693",
		"publisher": "University of Michigan Press",
		"publisher-place": "Ann Arbor",
		"source": "Open WorldCat",
		"title": "Interdisciplining digital humanities boundary work in an emerging field",
		"URL": "http://www.jstor.org/stable/10.2307/j.ctv65swxd",
		"author": [
			{
				"family": "Klein",
				"given": "Julie Thompson"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					7
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/3WXDAPTF",
		"type": "book",
		"abstract": "\"This book presents concepts and methods for computing cultural data, exploring digitized media and artifacts, and understanding astonishing scale of cultural growth in the digital era\"--",
		"call-number": "HM623 .M365 2020",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-03710-5",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "Cultural analytics",
		"author": [
			{
				"family": "Manovich",
				"given": "Lev"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/V7WH7K92",
		"type": "paper-conference",
		"container-title": "Digital Humanities 2017 Conference Abstracts",
		"event-place": "Montréal",
		"event-title": "Digital Humanities 2017",
		"language": "eng",
		"page": "335-336",
		"publisher-place": "Montréal",
		"title": "Micro DH: Digital Humanities at the Small Scale",
		"title-short": "Micro DH",
		"URL": "https://dh2017.adho.org/abstracts/196/196.pdf",
		"author": [
			{
				"family": "Risam",
				"given": "Roopika"
			},
			{
				"family": "Edwards",
				"given": "Susan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/HPU5M284",
		"type": "article-journal",
		"container-title": "Digital Scholarship in the Humanities",
		"issue": "suppl_1",
		"note": "ISBN: 2055-7671\npublisher: Oxford University Press",
		"page": "i4-i15",
		"title": "Digital humanities in the Anthropocene",
		"volume": "30",
		"author": [
			{
				"family": "Nowviskie",
				"given": "Bethany"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/NWSIX72J",
		"type": "article-journal",
		"container-title": "Studia Universitatis Babeș-Bolyai-Digitalia",
		"issue": "1",
		"note": "ISBN: 2559-6721\npublisher: Studia Universitatis Babes-Bolyai",
		"page": "83-88",
		"title": "A low te (a) ch approach to digital humanities",
		"volume": "62",
		"author": [
			{
				"family": "Pop",
				"given": "Liviu"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/H75CF7W3",
		"type": "article-journal",
		"title": "Adapting Minimal Computing Approaches for Public Humanities Projects: A New Take on the History Harvest Model",
		"author": [
			{
				"family": "Dalmau",
				"given": "Michelle"
			},
			{
				"family": "Kalani",
				"given": "Craig"
			},
			{
				"family": "Szostalo",
				"given": "Maksymilian"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/TEKHRDTL",
		"type": "paper-conference",
		"container-title": "DH",
		"title": "Accessing Alternative Histories and Futures: Afro-Latin American Models for the Digital Humanities.",
		"author": [
			{
				"family": "Arriaga",
				"given": "Eduard A."
			},
			{
				"family": "Villar",
				"given": "Andrés"
			},
			{
				"family": "Captain-Hidalgo",
				"given": "Yvone"
			},
			{
				"family": "Martino",
				"given": "Maria Cecilia"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6Q9Z2AXE",
		"type": "article-journal",
		"container-title": "Digital Scholarship in History and the Humanities",
		"page": "82",
		"title": "go rich:: go minimal",
		"author": [
			{
				"family": "Caria",
				"given": "Federico"
			}
		]
	},
	{
		"id": "http://zotero.org/users/163570/items/KQDLQLY6",
		"type": "article-journal",
		"container-title": "Fudan Journal of the Humanities and Social Sciences",
		"issue": "3",
		"note": "ISBN: 2198-2600\npublisher: Springer",
		"page": "357-369",
		"title": "Digital humanities within a global context: creating borderlands of localized expression",
		"volume": "11",
		"author": [
			{
				"family": "Earhart",
				"given": "Amy E."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/J3IJTPRW",
		"type": "article-journal",
		"container-title": "DHQ: Digital Humanities Quarterly",
		"issue": "1",
		"note": "ISBN: 1938-4122",
		"title": "Healing the Gap: Digital Humanities Methods for the Virtual Reunification of Split Media and Paper Collections.",
		"volume": "15",
		"author": [
			{
				"family": "Sapienza",
				"given": "Stephanie"
			},
			{
				"family": "Hoyt",
				"given": "Eric"
			},
			{
				"family": "St John",
				"given": "Matt"
			},
			{
				"family": "Summers",
				"given": "Ed"
			},
			{
				"family": "Bersch",
				"given": "J. J."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9DZJF2G3",
		"type": "article-journal",
		"note": "publisher: Indiana University Digital Collections Services",
		"title": "Minimal Computing Approaches for Public Humanities Projects: A New Take on the History Harvest Model",
		"author": [
			{
				"family": "Dalmau",
				"given": "Michelle"
			},
			{
				"family": "Szostalo",
				"given": "Maks"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6R89DWVZ",
		"type": "article-journal",
		"container-title": "Scholarly and Research Communication",
		"issue": "2/3",
		"note": "ISBN: 1923-0702",
		"title": "Revisiting Open Source Software Development Models for Community-Based Digital Humanities Research Generation",
		"volume": "7",
		"author": [
			{
				"family": "Lane",
				"given": "Richard J."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7UACSGLM",
		"type": "paper-conference",
		"container-title": "Music Encoding Conference 2020",
		"title": "MEI and Verovio for MIR: A Minimal Computing Approach",
		"author": [
			{
				"family": "Saccomano",
				"given": "Mark"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5BBGXDY2",
		"type": "paper-conference",
		"container-title": "Global Digital Humanities Symposium 2021",
		"title": "Teaching digital scholarly editing North and South in a Global Classroom",
		"author": [
			{
				"family": "De Léon",
				"given": "Romina"
			},
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			},
			{
				"family": "Hernández",
				"given": "Nidia"
			},
			{
				"family": "Viglianti",
				"given": "Raffaele"
			}
		]
	},
	{
		"id": "http://zotero.org/users/163570/items/KZGNMZQ3",
		"type": "article-journal",
		"title": "Introduction to Digital Humanities Syllabus",
		"author": [
			{
				"family": "Gold",
				"given": "Matthew K."
			},
			{
				"family": "Josephs",
				"given": "Kelly"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Q2R8IYXX",
		"type": "chapter",
		"container-title": "Debates in the Digital Humanities",
		"event-place": "Minneapolis",
		"page": "437-441",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"title": "DH Adjuncts: Social Justice and Care",
		"author": [
			{
				"family": "Berens",
				"given": "Kathi Inman"
			}
		],
		"editor": [
			{
				"family": "Gold",
				"given": "Matthew K."
			},
			{
				"family": "Klein",
				"given": "Lauren F."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/UWI8RQ3B",
		"type": "paper-conference",
		"container-title": "Access Conference Proceedings",
		"title": "Minimal Computing+ Libraries",
		"author": [
			{
				"family": "Severson",
				"given": "Sarah"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9RNC8SWS",
		"type": "paper-conference",
		"container-title": "DH2020 carrefours/intersections",
		"title": "MAZI means together: An open-source “minimal computing” local community network for cultural event organisation, fieldwork research and digital curatorial practices",
		"author": [
			{
				"family": "Brailas",
				"given": "Alexis"
			},
			{
				"family": "Leventaki",
				"given": "Elli"
			},
			{
				"family": "Ziku",
				"given": "Mariana"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/V8G9WE4L",
		"type": "thesis",
		"event-place": "New York",
		"genre": "Capstone Project",
		"language": "En",
		"publisher": "The City University of New York",
		"publisher-place": "New York",
		"title": "DH  in Prison",
		"URL": "https://academicworks.cuny.edu/gc_etds/3787",
		"author": [
			{
				"family": "Pringle",
				"given": "Sabina"
			}
		],
		"contributor": [
			{
				"family": "Gold",
				"given": "Matthew K."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020",
					6
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ABEWHU3W",
		"type": "post-weblog",
		"container-title": "Minimal Computing: a working group of GO::DH",
		"language": "en",
		"title": "The User, the Learner and the Machines We Make",
		"URL": "http://go-dh.github.io/mincomp/thoughts/2015/05/21/user-vs-learner/",
		"author": [
			{
				"family": "Gil",
				"given": "Alex"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015",
					5,
					21
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/XTTDWM9C",
		"type": "article-journal",
		"abstract": "My research bridges my interests in media history, in particular history of the book, with my duties helping catalyze conversations around digital humanities, diversity, and social justice in an academic library at a large public university. This summer’s reading has gelled around a couple of slowly converging topics – information literacy and minimal computing in DH pedagogy, and representations of AIDS in late 80s-early 90s countercultures. I’m interested in theorizing DH praxis, as well as understanding how technology implicates its users in systems of power.",
		"container-title": "dh + lib review",
		"ISSN": "2380-1255",
		"language": "en-US",
		"note": "publisher: ACRL",
		"source": "hcommons.org",
		"title": "What I’m Reading This Summer: Spencer Keralis",
		"title-short": "What I’m Reading This Summer",
		"URL": "https://hcommons.org/deposits/item/hc:14877/",
		"author": [
			{
				"family": "Keralis",
				"given": "Spencer"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2017",
					7,
					25
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WKM2EQFU",
		"type": "article-journal",
		"abstract": "This research addresses the issues surrounding the low level of Digital Humanities (DH) technological consciousness among students and academics in the humanities discipline in Africa (Nigeria). The study, using online questionnaires, shows that despite the wide acceptance of DH Technological tools among some African scholars in the humanities, there are still challenges experienced by these Scholars in the course of using some of these DH tools to capture African realities. These difficulties include low level of training for users of DH technologies in Africa, as well as the designers' failure to optimize those tools for use in the analysis of data, texts, and images extracted in Africa. To address these constraints, this research enjoins African scholars to come up with epistemological and ontological frameworks that would aid software developers in creating tools which capture the unique aspects of African history, techne, culture, philosophy and tradition.",
		"language": "en-US",
		"source": "hcommons.org",
		"title": "DIGITAL HUMANITIES SCHOLARSHIP IN AFRICA: Prospects and Challenges",
		"title-short": "DIGITAL HUMANITIES SCHOLARSHIP IN AFRICA",
		"URL": "https://hcommons.org/deposits/item/hc:32033/",
		"author": [
			{
				"family": "Farinola",
				"given": "Augustine"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020",
					7
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/8F9H399H",
		"type": "software",
		"genre": "Python",
		"license": "GPL-3.0",
		"note": "original-date: 2014-12-12T21:08:09Z",
		"publisher": "Laboratorio Experimental (ITCR @ SIUA)",
		"source": "GitHub",
		"title": "LibreScan",
		"URL": "https://github.com/labexp/LibreScan",
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2021",
					8,
					12
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/J3S75DIZ",
		"type": "software",
		"genre": "C++",
		"note": "original-date: 2014-04-06T17:32:27Z",
		"publisher": "scantailor",
		"source": "GitHub",
		"title": "Scan Tailor - scantailor.org",
		"URL": "https://github.com/scantailor/scantailor",
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/F68EEZPZ",
		"type": "webpage",
		"abstract": "Hi, I am a fan of the old tool and created this as a fan page, I found some of the old info on the old website and posted it here to help people and developers looking for it. Remember I am just a fan so do not contact me for help or additional info. […]",
		"container-title": "ScanTailor",
		"language": "en-US",
		"title": "ScanTailor",
		"URL": "https://scantailor.org/",
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7EU22BMV",
		"type": "webpage",
		"title": "DIY Book Scanner - Index page",
		"URL": "https://diybookscanner.org/forum/",
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BT7XQXDI",
		"type": "article-journal",
		"title": "Style revolution: a new approach to digital scholarship and collection-building at the Columbia University Libraries",
		"author": [
			{
				"family": "Levin",
				"given": "Meredith"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Y5JNR73Z",
		"type": "paper-conference",
		"container-title": "Proceedings of theXVII Workshop de Software Livre, WSL",
		"title": "LibreScan: Software Libre para la digitalización de documentos utilizando escáneres de bajo costo",
		"author": [
			{
				"family": "Alfaro",
				"given": "Jaime Gutiérrez"
			},
			{
				"family": "Rodrıguez",
				"given": "Aurelio Sanabria"
			},
			{
				"family": "Avila",
				"given": "Diego Ugalde"
			},
			{
				"family": "Méndez",
				"given": "Daniel Solıs"
			},
			{
				"family": "Pérez",
				"given": "Melvin Elizondo"
			},
			{
				"family": "Hsu",
				"given": "Tony Kong"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VT6N3P49",
		"type": "thesis",
		"event-place": "Valencia",
		"genre": "Tesis de Maestría",
		"language": "es",
		"note": "publisher: Universitat Politècnica de València",
		"publisher": "Universitat Politècnica de València",
		"publisher-place": "Valencia",
		"title": "Desarrollo de un escritorio digital para la captura, transcripción y gestión multimodal e interactiva de documentos manuscritos",
		"URL": "http://hdl.handle.net/10251/44381",
		"author": [
			{
				"family": "Vicente Parra",
				"given": "Francisco Javier"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2014"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6RI84JX5",
		"type": "article-journal",
		"container-title": "AI & SOCIETY",
		"DOI": "https://doi.org/10.1007/s00146-021-01372-0",
		"issue": "37",
		"journalAbbreviation": "AI & Soc",
		"note": "ISBN: 1435-5655\npublisher: Springer",
		"page": "949–958",
		"title": "The role of born digital data in confronting a difficult and contested past through digital storytelling: the Waterford Memories Project",
		"author": [
			{
				"family": "O’Mahoney",
				"given": "Jennifer"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/NCL5PY27",
		"type": "article-journal",
		"abstract": "Digital Humanities (DH) has come a long way towards establishing itself as a dynamic and innovative field of study. However, it has been pointed out that the DH community predominantly comprises scholars from a handful of mainly English-speaking countries, and a current challenge is achieving a broader internationalization of the DH community. This article provides an overview of the landscape in terms of geo-linguistic diversity, as well as reviewing current DH initiatives to broaden regional and linguistic diversity and identifies some of the main challenges ahead. The aim of this article is to serve as a benchmark of the current situation and suggest areas where further research is required.",
		"container-title": "Literary and Linguistic Computing",
		"DOI": "10.1093/llc/fqu005",
		"ISSN": "0268-1145",
		"issue": "3",
		"journalAbbreviation": "Literary and Linguistic Computing",
		"page": "307-316",
		"source": "Silverchair",
		"title": "Geographical and linguistic diversity in the Digital Humanities",
		"URL": "https://doi.org/10.1093/llc/fqu005",
		"volume": "29",
		"author": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2014",
					9,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9ZHBJS4F",
		"type": "article-journal",
		"abstract": "In recent years, the question of what it means to “decolonize” digital humanities has been broached by scholars engaged in both postcolonial digital humanities and #TransformDH, strands of the field that have pushed for greater attention to digital humanities projects and methods that foreground intersectional engagement with race, gender, class, sexuality, nation, disability, and other axes of identity that shape knowledge production. Such approaches to digital humanities have asked how to decolonize the archive (Povinelli 2011; Lothian & Phillips 2013; Cushman 2013; cárdenas et al. 2015; Risam 2015), address gaps in knowledge produced online (Lor and Britz 2005; Sheppard 2005; Koh & Risam 2013), make legible narratives and histories that have gone untold (Rawson 2014; Thorat 2015; Verhoeven 2015), understand the specificities of digital Dalit experience (Nayar 2011), locate the subaltern in cyberspace (Gajjala 2013), or use technologies to push back against existing forms of representation that may be troubling (Sanders 2014; Priego & Gil 2013; Olsen 2014). Taking a look at the theoretical basis of such work in both postcolonial and science and technology studies (STS), this chapter situates the stakes for decolonization within digital humanities, locating a historical scholarly genealogy for this work and outlining what work toward decolonization looks like in practice within digital humanities.",
		"container-title": "The Routledge Companion to Media Studies and Digital Humanities",
		"language": "en",
		"note": "Accepted: 2021-11-29T11:25:44Z",
		"source": "digitalrepository.salemstate.edu",
		"title": "Decolonizing The Digital Humanities In Theory And Practice",
		"URL": "https://digitalrepository.salemstate.edu/handle/20.500.13013/421",
		"author": [
			{
				"family": "Risam",
				"given": "Roopika"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018",
					5,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/CL9AXC8I",
		"type": "article-journal",
		"abstract": "Digital Humanities as a Critical Project: The Importance and Some Problems of a Literary Criticism Perspective on Computational Approaches [James E. Dobson, Critical Digital Humanities, 2019]",
		"container-title": "JLTonline Reviews",
		"ISSN": "1862-8990",
		"issue": "0",
		"language": "en",
		"license": "Authors who publish reviews with this journal agree to the following terms:    Authors retain copyright and grant the journal right of first publication with the work simultaneously licensed under a   Creative Commons Attribution License   that allows others to share the work with an acknowledgement of the work's authorship and initial publication in this journal.  Authors are able to enter into separate, additional contractual arrangements for the non-exclusive distribution of the journal's published version of the work (e.g., post it to an institutional repository or publish it in a book), with an acknowledgement of its initial publication in this journal.  Authors are permitted and encouraged to post their work online (e.g., in institutional repositories or on their website) prior to and during the submission process, as it can lead to productive exchanges, as well as earlier and greater citation of published work.   Please note that there is a different set of terms for authors who publish articles other than reviews for this journal (see Articles section).",
		"note": "number: 0",
		"source": "www.jltonline.de",
		"title": "Digital Humanities as a Critical Project: The Importance and Some Problems of a Literary Criticism Perspective on Computational Approaches [James E. Dobson, Critical Digital Humanities, 2019]",
		"title-short": "Digital Humanities as a Critical Project",
		"URL": "http://www.jltonline.de/index.php/reviews/article/view/1033",
		"volume": "0",
		"author": [
			{
				"family": "Gius",
				"given": "Evelyn"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020",
					1,
					24
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9MTTBF6J",
		"type": "book",
		"abstract": "\"Can established humanities methods coexist with computational thinking? It is one of the major questions in humanities research today, as scholars increasingly adopt sophisticated data science for their work. James E. Dobson explores the opportunities and complications faced by humanists in this new era. Though the study and interpretation of texts alongside sophisticated computational tools can serve scholarship, these methods cannot replace existing frameworks. As Dobson shows, ideas of scientific validity cannot easily nor should be adapted for humanities research because digital humanities, unlike science, lack a leading-edge horizon charting the frontiers of inquiry. Instead, the methods of digital humanities require a constant rereading. At the same time, suspicious and critical readings of digital methodologies make it unwise for scholars to defer to computational methods. Humanists must examine the tools--including the assumptions that went into the codes and algorithms--and questions surrounding their own use of digital technology in research. Insightful and forward thinking, this book lays out a new path of humanistic inquiry that merges critical theory and computational science\"--",
		"call-number": "AZ105 .D59 2019",
		"collection-title": "Topics in the digital humanities",
		"event-place": "Urbana, Illinois",
		"ISBN": "978-0-252-04227-0",
		"number-of-pages": "175",
		"publisher": "University of Illinois Press",
		"publisher-place": "Urbana, Illinois",
		"source": "Library of Congress ISBN",
		"title": "Critical Digital Humanities: The Search for a Methodology",
		"title-short": "Critical Digital Humanities",
		"author": [
			{
				"family": "Dobson",
				"given": "James E."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JRPNQMGM",
		"type": "chapter",
		"container-title": "A New Companion to Digital Humanities",
		"event-place": "West Sussex",
		"page": "3-21",
		"publisher": "Wiley",
		"publisher-place": "West Sussex",
		"title": "Between Bits and Atoms: Physical Computing and Desktop Fabrication in the Humanities",
		"title-short": "Between Bits and Atoms",
		"author": [
			{
				"family": "Sayers",
				"given": "Jentery"
			},
			{
				"family": "Elliott",
				"given": "Devon"
			},
			{
				"family": "Kraus",
				"given": "Kari"
			},
			{
				"family": "Nowviskie",
				"given": "Bethany"
			},
			{
				"family": "Turkel",
				"given": "William J."
			}
		],
		"editor": [
			{
				"family": "Schreibman",
				"given": "Susan"
			},
			{
				"family": "Siemens",
				"given": "Ray"
			},
			{
				"family": "Unsworth",
				"given": "John"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/MQQ4RDT2",
		"type": "paper-conference",
		"container-title": "Digital Humanities 2016: Conference Abstracts",
		"event-place": "Kraków",
		"event-title": "Digital Humanities 2016",
		"page": "943-944",
		"publisher": "Jagiellonian University & Pedagogical University",
		"publisher-place": "Kraków",
		"title": "Minimal Computing: A Workshop",
		"URL": "https://dh2016.adho.org/abstracts/304",
		"author": [
			{
				"family": "Gil",
				"given": "Alex"
			},
			{
				"family": "Sayers",
				"given": "Jentery"
			},
			{
				"family": "Martin",
				"given": "K"
			},
			{
				"family": "Rosenblum",
				"given": "B"
			},
			{
				"family": "Chan",
				"given": "T"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ATH289W7",
		"type": "chapter",
		"container-title": "Global Debates in the Digital Humanities",
		"event-place": "Minneapolis",
		"page": "259-270",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"title": "Site-Specific Cultural Infrastructure. Promoting Access and Conquering the Digital  Divide",
		"author": [
			{
				"family": "Steyn",
				"given": "Juan"
			},
			{
				"family": "Goodrich",
				"given": "Andre"
			}
		],
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/3XPRV5LG",
		"type": "chapter",
		"container-title": "Global Debates in the Digital Humanities",
		"event-place": "Minneapolis",
		"page": "247-258",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"title": "Digital Humanities and Visible and Invisible Infrastructures",
		"author": [
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Q2TC6A7L",
		"type": "chapter",
		"abstract": "Ian Hodder (2014) recently pointed to a “return to things” in the humanities and social sciences—a mode of analysis that explores the relationships between people and the objects we use to construct and make sense of the world (19). In digital humanities (DH), we see this turn in Matthew Kirschenbaum’s (2007) forensic analysis of computer hard disks; platform studies that investigate the relationship between computing culture, consoles, and other hardware (Monfort and Bogost 2009); and maker cultures that explore the humanities through practical experimentation (Dieter and Lovink 2014). A return to things suggests a desire to pay attention to",
		"collection-title": "Experiments in the Digital Humanities",
		"container-title": "Making Things and Drawing Boundaries",
		"ISBN": "978-1-5179-0285-8",
		"note": "DOI: 10.5749/j.ctt1pwt6wq.13",
		"page": "102-114",
		"publisher": "University of Minnesota Press",
		"source": "JSTOR",
		"title": "Full Stack DH: Building a Virtual Research Environment on a Raspberry Pi",
		"title-short": "Full Stack DH",
		"URL": "https://www.jstor.org.pbidi.unam.mx:8080/stable/10.5749/j.ctt1pwt6wq.13",
		"author": [
			{
				"family": "Smithies",
				"given": "James"
			}
		],
		"editor": [
			{
				"family": "Sayers",
				"given": "Jentery"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/B6LXNQR5",
		"type": "paper-conference",
		"event-title": "2018 MLA Annual Convention",
		"publisher": "MLA",
		"source": "mla.confex.com",
		"title": "Activist Infrastructures: Vulnerable Collections and Minimal Computing",
		"title-short": "<span>Activist Infrastructures",
		"URL": "https://mla.confex.com/mla/2018/meetingapp.cgi/Session/2310",
		"author": [
			{
				"family": "Ortega",
				"given": "Élika"
			},
			{
				"family": "Gil",
				"given": "Alexander"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					4,
					8
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018",
					1,
					5
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/TZ8N4LNH",
		"type": "book",
		"call-number": "PN56.P555 R57 2019",
		"event-place": "Evanston, Illinois",
		"ISBN": "978-0-8101-3886-5",
		"number-of-pages": "176",
		"publisher": "Northwestern University Press",
		"publisher-place": "Evanston, Illinois",
		"source": "Library of Congress ISBN",
		"title": "New digital worlds: postcolonial digital humanities in theory, praxis, and pedagogy",
		"title-short": "New digital worlds",
		"author": [
			{
				"family": "Risam",
				"given": "Roopika"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5VJTHTTS",
		"type": "chapter",
		"collection-title": "De gruyter reference",
		"container-title": "Handbook digital public history",
		"edition": "1",
		"event-place": "Boston",
		"ISBN": "978-3-11-043922-9",
		"page": "301-308",
		"publisher": "De Gruyter Oldenbourg",
		"publisher-place": "Boston",
		"source": "Library of Congress ISBN",
		"title": "Mapping and Maps in Digital and Public History",
		"editor": [
			{
				"family": "Noiret",
				"given": "Serge"
			},
			{
				"family": "Tebeau",
				"given": "Mark"
			},
			{
				"family": "Zaagsma",
				"given": "Gerben"
			}
		],
		"author": [
			{
				"family": "Gibbs",
				"given": "Fred"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/TL8JYG89",
		"type": "chapter",
		"abstract": "\"An illuminating volume of critical essays charting the diverse territory of digital humanities scholarship\"--",
		"call-number": "AZ105 .P43 2021",
		"container-title": "People, practice, power: digital humanities outside the center",
		"event-place": "Minneapolis",
		"ISBN": "978-1-5179-1067-9",
		"page": "58-69",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Laboratory. A New Space in Digital Humanities",
		"editor": [
			{
				"family": "Nieves",
				"given": "Angel David"
			},
			{
				"family": "McGrail",
				"given": "Anne B."
			},
			{
				"family": "Senier",
				"given": "Siobhan"
			}
		],
		"author": [
			{
				"family": "Pawlicka-Deger",
				"given": "Urszula"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/4JKM9HFU",
		"type": "book",
		"event-place": "Ann Arbor, MI",
		"ISBN": "978-0-472-07254-5",
		"language": "en",
		"note": "DOI: 10.3998/dh.12869322.0001.001",
		"publisher": "digitalculturebooks",
		"publisher-place": "Ann Arbor, MI",
		"source": "DOI.org (Crossref)",
		"title": "Interdisciplining Digital Humanities: Boundary Work in an Emerging Field",
		"title-short": "Interdisciplining Digital Humanities",
		"URL": "https://www.fulcrum.org/concern/monographs/2b88qd07q",
		"author": [
			{
				"family": "Klein",
				"given": "Julie"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					5,
					12
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/4UGFNSFP",
		"type": "chapter",
		"abstract": "This chapter discusses the notion of collocation graphs and networks, which not only represent visualisation of the collocational relationship traditionally displayed in a tabular form but also constitute a novel analytical technique. This technique, although originally proposed by Philips in 1985, has only recently gained prominence with the introduction of the #LancsBox tool (Brezina et al., Int J Corpus Linguist 20:139–173, 2015), which can, among other things, build collocation graphs and networks on the fly. Simple collocation graphs and collocation networks show association and cross-association between words in language and discourse and can thus be used in a range of areas of linguistic and social research. This chapter demonstrates the use of the collocation network technique in (i) discourse analysis, (ii) language learning research and (iii) lexicography, providing three case studies that focus not only on the variety of applications but also on different methodological choices involved in using the technique.",
		"collection-title": "Quantitative Methods in the Humanities and Social Sciences",
		"container-title": "Lexical Collocation Analysis: Advances and Applications",
		"event-place": "Cham",
		"ISBN": "978-3-319-92582-0",
		"language": "en",
		"note": "DOI: 10.1007/978-3-319-92582-0_4",
		"page": "59-83",
		"publisher": "Springer International Publishing",
		"publisher-place": "Cham",
		"source": "Springer Link",
		"title": "Collocation Graphs and Networks: Selected Applications",
		"title-short": "Collocation Graphs and Networks",
		"URL": "https://doi.org/10.1007/978-3-319-92582-0_4",
		"author": [
			{
				"family": "Brezina",
				"given": "Vaclav"
			}
		],
		"editor": [
			{
				"family": "Cantos-Gómez",
				"given": "Pascual"
			},
			{
				"family": "Almela-Sánchez",
				"given": "Moisés"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					5,
					27
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/PFWNQKP8",
		"type": "book",
		"abstract": "A visionary report on the revitalization of the liberal arts tradition in the electronically inflected, design-driven, multimedia language of the twenty-first century.",
		"event-place": "Cambridge, MA, USA",
		"ISBN": "978-0-262-01847-0",
		"language": "en",
		"number-of-pages": "152",
		"publisher": "MIT Press",
		"publisher-place": "Cambridge, MA, USA",
		"source": "MIT Press Books",
		"title": "Digital_Humanities",
		"author": [
			{
				"family": "Burdick",
				"given": "Anne"
			},
			{
				"family": "Drucker",
				"given": "Johanna"
			},
			{
				"family": "Lunenfeld",
				"given": "Peter"
			},
			{
				"family": "Presner",
				"given": "Todd"
			},
			{
				"family": "Jeffrey",
				"given": "Schnapp"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/IBHQJBID",
		"type": "book",
		"edition": "paperback edition",
		"ISBN": "978-0-262-52886-3",
		"language": "eng",
		"source": "K10plus ISBN",
		"title": "Digital humanities",
		"editor": [
			{
				"family": "Burdick",
				"given": "Anne"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WFP8YLSJ",
		"type": "article-journal",
		"abstract": "This paper aims to reflect the growing importance of the term \"digital humanities\", whether defined as a disciplinary field, a training profile or a movement linked to open access. Although closely related to library and information science, digital humanities is often used in projects without the collaboration of libraries. Developing specific support centres is one way to facilitate libraries' cooperation and participation in digital humanities projects.",
		"ISSN": "1886-6344",
		"language": "spa",
		"license": "openAccess",
		"note": "Accepted: 2013-06-04T12:48:40Z",
		"source": "digital.csic.es",
		"title": "Humanidades digitales, ¿una mera etiqueta o un campo por el que deben apostar las ciencias de la documentación?",
		"URL": "https://digital.csic.es/handle/10261/77511",
		"author": [
			{
				"family": "Rodríguez Yunta",
				"given": "Luis"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					5,
					23
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/DM6F63PT",
		"type": "speech",
		"title": "Las Humanidades Digitales en el contexto de la  Ciencia Abierta",
		"URL": "https://www.cepal.org/sites/default/files/news/files/20190926_del_rio_gimena_hdyca.pdf",
		"author": [
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019",
					9,
					26
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/8W4CP6BN",
		"type": "article-journal",
		"abstract": "Although digital humanities (DH) has received a lot of attention in recent years, its status as “a discipline in its own right” (Schreibman et al., A companion to digital humanities (pp. xxiii–xxvii). Blackwell; 2004) and its position in the overall academic landscape are still being negotiated. While there are countless essays and opinion pieces that debate the status of DH, little research has been dedicated to exploring the field in a systematic and empirical way (Poole, Journal of Documentation; 2017:73). This study aims to contribute to the existing research gap by comparing articles published over the past three decades in three established English-language DH journals (Computers and the Humanities, Literary and Linguistic Computing, Digital Humanities Quarterly) with research articles from journals in 15 other academic disciplines (corpus size: 34,041 articles; 299 million tokens). As a method of analysis, we use latent Dirichlet allocation topic modeling, combined with recent approaches that aggregate topic models by means of hierarchical agglomerative clustering. Our findings indicate that DH is simultaneously a discipline in its own right and a highly interdisciplinary field, with many connecting factors to neighboring disciplines—first and foremost, computational linguistics, and information science. Detailed descriptive analyses shed some light on the diachronic development of DH and also highlight topics that are characteristic for DH.",
		"container-title": "Journal of the Association for Information Science and Technology",
		"DOI": "10.1002/asi.24533",
		"ISSN": "2330-1643",
		"issue": "2",
		"language": "en",
		"note": "_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/asi.24533",
		"page": "148-171",
		"source": "Wiley Online Library",
		"title": "Digital humanities—A discipline in its own right? An analysis of the role and position of digital humanities in the academic landscape",
		"title-short": "Digital humanities—A discipline in its own right?",
		"URL": "https://onlinelibrary.wiley.com/doi/abs/10.1002/asi.24533",
		"volume": "73",
		"author": [
			{
				"family": "Luhmann",
				"given": "Jan"
			},
			{
				"family": "Burghardt",
				"given": "Manuel"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					5,
					23
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/2PKREBE4",
		"type": "book",
		"abstract": "\"The Digital Humanities is a comprehensive introduction and practical guide to how humanists use the digital to conduct research, organize materials, analyze, and publish findings. It summarizes the turn toward the digital that is reinventing every aspect of the humanities among scholars, libraries, publishers, administrators, and the public. Beginning with some definitions and a brief historical survey of the humanities, the book examines how humanists work, what they study, and how humanists and their research have been impacted by the digital and how, in turn, they shape it. It surveys digital humanities tools and their functions, the digital humanists' environments, and the outcomes and reception of their work. The book pays particular attention to both theoretical underpinnings and practical considerations for embarking on digital humanities projects. It places the digital humanities firmly within the historical traditions of the humanities and in the contexts of current academic and scholarly life\"--",
		"call-number": "AZ105 .G37 2015",
		"event-place": "New York, NY",
		"ISBN": "978-1-107-01319-3",
		"number-of-pages": "273",
		"publisher": "Cambridge University Press",
		"publisher-place": "New York, NY",
		"source": "Library of Congress ISBN",
		"title": "The digital humanities: a primer for students and scholars",
		"title-short": "The digital humanities",
		"author": [
			{
				"family": "Gardiner",
				"given": "Eileen"
			},
			{
				"family": "Musto",
				"given": "Ronald G."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/JXE37AF6",
		"type": "article-journal",
		"abstract": "Purchase online the PDF of La transformación neoliberal de la ciencia : El caso de las Humanidades Digitales, Aibar Puentes, Eduard - Ediciones Universidad de Salamanca - Article",
		"container-title": "La transformación neoliberal de la ciencia : El caso de las Humanidades Digitales",
		"language": "en",
		"note": "publisher: Ediciones Universidad de Salamanca",
		"page": "13-28",
		"source": "www.torrossa.com",
		"title": "La transformación neoliberal de la ciencia : El caso de las Humanidades Digitales",
		"title-short": "La transformación neoliberal de la ciencia",
		"URL": "https://www.torrossa.com/en/resources/an/4371249",
		"author": [
			{
				"family": "Aibar Puentes",
				"given": "Eduard"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					8,
					10
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BXLVVK4E",
		"type": "chapter",
		"container-title": "Pautas para el desarrollo y la evaluación de proyectos digitales en las humanidades",
		"page": "53–70",
		"publisher": "CDMX: Instituto de Investigaciones Bibliográficas",
		"source": "PhilPapers",
		"title": "¿Cómo reconocer un proyecto de Humanidades Digitales?",
		"title-short": "?",
		"author": [
			{
				"family": "Barrón",
				"given": "Francisco"
			}
		],
		"editor": [
			{
				"family": "Galina",
				"given": "Isabel"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/2MBLJVGK",
		"type": "article-journal",
		"abstract": "Antes que hablar de humanidades digitales, este artículo propone contextualizarlas críticamente revisando cuestiones relacionadas con la geopolítica del conocimiento y las desigualdades en la investigación a nivel global. Para ello, interroga etiquetas acuñadas desde el norte y piensa el sur o los sures como parte de la epistemología de unas humanidades digitales independientes y sostenibles.",
		"ISSN": "2237-8723",
		"language": "spa",
		"license": "info:eu-repo/semantics/openAccess",
		"note": "Accepted: 2022-07-19T11:35:13Z\npublisher: Arquivo Nacional",
		"source": "ri.conicet.gov.ar",
		"title": "Una vez más sobre los sures de las Humanidades Digitales",
		"URL": "https://ri.conicet.gov.ar/handle/11336/162451",
		"author": [
			{
				"family": "Rio",
				"given": "María Gimena",
				"non-dropping-particle": "del"
			},
			{
				"family": "Fiormonte",
				"given": "Domenico"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					8,
					10
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022",
					3
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/FIN8QQIU",
		"type": "chapter",
		"abstract": "\"This collection addresses the lack of perspectives beyond Westernized and Anglophone contexts in the digital humanities. Focused on work that has been underappreciated for linguistic, cultural, or geopolitical reasons, contributors showcase alternative histories that detail the rise of the digital humanities in the Global South and other \"invisible\" contexts and explore the implications of a truly global digital humanities\"--",
		"call-number": "AZ105",
		"collection-title": "Debates in the digital humanities",
		"container-title": "Global debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-1-4529-6710-3",
		"page": "23-48",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Technology and the humanities: A history of interaction",
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/S88DAMBJ",
		"type": "chapter",
		"abstract": "\"This collection addresses the lack of perspectives beyond Westernized and Anglophone contexts in the digital humanities. Focused on work that has been underappreciated for linguistic, cultural, or geopolitical reasons, contributors showcase alternative histories that detail the rise of the digital humanities in the Global South and other \"invisible\" contexts and explore the implications of a truly global digital humanities\"--",
		"call-number": "AZ105",
		"collection-title": "Debates in the digital humanities",
		"container-title": "Global debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-1-4529-6710-3",
		"page": "247-258",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Digital Humanities and Visible and Invisible Infrastructures",
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"author": [
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/79WVXB5I",
		"type": "chapter",
		"abstract": "\"An illuminating volume of critical essays charting the diverse territory of digital humanities scholarship\"--",
		"call-number": "AZ105 .P43 2021",
		"container-title": "People, practice, power: digital humanities outside the center",
		"event-place": "Minneapolis",
		"ISBN": "978-1-5179-1067-9",
		"page": "3-23",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Epistemic Infrastructure, the Instrumental Turn, and the Digital Humanities",
		"editor": [
			{
				"family": "Nieves",
				"given": "Angel David"
			},
			{
				"family": "McGrail",
				"given": "Anne B."
			},
			{
				"family": "Senier",
				"given": "Siobhan"
			}
		],
		"author": [
			{
				"family": "Malazita",
				"given": "James"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QHXU3KRC",
		"type": "article-journal",
		"container-title": "Digital Humanities Quarterly",
		"ISSN": "1938-4122",
		"issue": "2",
		"journalAbbreviation": "DHQ",
		"title": "Minimizing Computing Maximizes Labor",
		"URL": "http://www.digitalhumanities.org/dhq/vol/16/2/000594/000594.html",
		"volume": "16",
		"author": [
			{
				"family": "Dombrowski",
				"given": "Quinn"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/DJKZN97U",
		"type": "chapter",
		"abstract": "\"This collection addresses the lack of perspectives beyond Westernized and Anglophone contexts in the digital humanities. Focused on work that has been underappreciated for linguistic, cultural, or geopolitical reasons, contributors showcase alternative histories that detail the rise of the digital humanities in the Global South and other \"invisible\" contexts and explore the implications of a truly global digital humanities\"--",
		"call-number": "AZ105",
		"collection-title": "Debates in the digital humanities",
		"container-title": "Global debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-1-4529-6710-3",
		"page": "101-114",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Digital Social Sciences and Digital Humanities of the South. Materials for a Critical Discussion",
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"author": [
			{
				"family": "Rodríguez-Ortega",
				"given": "Nuria"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/LUSKZAUS",
		"type": "book",
		"abstract": "\"This collection addresses the lack of perspectives beyond Westernized and Anglophone contexts in the digital humanities. Focused on work that has been underappreciated for linguistic, cultural, or geopolitical reasons, contributors showcase alternative histories that detail the rise of the digital humanities in the Global South and other \"invisible\" contexts and explore the implications of a truly global digital humanities\"--",
		"call-number": "AZ105",
		"collection-title": "Debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-1-4529-6710-3",
		"number-of-pages": "1",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Global debates in the digital humanities",
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/4CYM5B7U",
		"type": "chapter",
		"call-number": "AZ105 .B44 2015",
		"container-title": "Between humanities and the digital",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-02868-4",
		"page": "35-40",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "Humanities in the Digital Age",
		"editor": [
			{
				"family": "Svensson",
				"given": "Patrik"
			},
			{
				"family": "Goldberg",
				"given": "David Theo"
			}
		],
		"author": [
			{
				"family": "Liu",
				"given": "Alan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/3M4Z3XYR",
		"type": "book",
		"call-number": "AZ182 .D44 2012",
		"event-place": "Minneapolis",
		"ISBN": "978-0-8166-7794-8",
		"number-of-pages": "516",
		"publisher": "Univ Of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Debates in the digital humanities",
		"editor": [
			{
				"family": "Gold",
				"given": "Matthew K."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VQ677XKX",
		"type": "chapter",
		"call-number": "AZ182 .D44 2012",
		"container-title": "Debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-0-8166-7794-8",
		"page": "36-47",
		"publisher": "Univ Of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Beyond the Big Tent",
		"editor": [
			{
				"family": "Gold",
				"given": "Matthew K."
			}
		],
		"author": [
			{
				"family": "Svensson",
				"given": "Patrick"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/M3DB9PPB",
		"type": "book",
		"call-number": "AZ105 .D44 2013",
		"event-place": "Farnham, Surrey, England : Burlington, VT",
		"ISBN": "978-1-4094-6962-9",
		"number-of-pages": "314",
		"publisher": "Ashgate Publishing Limited ; Ashgate Publishing Company",
		"publisher-place": "Farnham, Surrey, England : Burlington, VT",
		"source": "Library of Congress ISBN",
		"title": "Defining digital humanities: a reader",
		"title-short": "Defining digital humanities",
		"editor": [
			{
				"family": "Terras",
				"given": "Melissa M."
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/74WIT8LF",
		"type": "chapter",
		"call-number": "AZ105 .D44 2013",
		"container-title": "Defining digital humanities: a reader",
		"event-place": "Farnham, Surrey, England : Burlington, VT",
		"ISBN": "978-1-4094-6962-9",
		"publisher": "Ashgate Publishing Limited ; Ashgate Publishing Company",
		"publisher-place": "Farnham, Surrey, England : Burlington, VT",
		"source": "Library of Congress ISBN",
		"title": "Peering inside the Big Tent",
		"editor": [
			{
				"family": "Terras",
				"given": "Melissa M."
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"author": [
			{
				"family": "Terras",
				"given": "Melissa"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9BHN3QV2",
		"type": "post-weblog",
		"abstract": "(cross-posted from http://paigemorgan.net)At DHSI 2014, participants requested an unconference session on how to turn a digital humanities project from an idea into a reality, and I offered to lead it. Here, roughly, are the steps that I recommended. A few are relevant chiefly to graduate students; most are applicable to academics at nearly any level. Some of these are",
		"container-title": "HASTAC",
		"language": "en",
		"title": "How to get a digital humanities project off the ground",
		"URL": "https://www.hastac.org/blogs/paigecm/2014/06/06/how-get-digital-humanities-project-ground",
		"author": [
			{
				"family": "Morgan",
				"given": "Paige"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					8,
					10
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2014",
					6,
					6
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/GF4T4QVW",
		"type": "book",
		"abstract": "\"A project-based introduction to programming in Python, with exercises. Covers general programming concepts, Python fundamentals, and problem solving. Includes three projects - how to create a simple video game, use data visualization techniques to make graphs and charts, and build an interactive web application\"--",
		"call-number": "QA76.73.P98 M38 2016",
		"event-place": "San Francisco",
		"ISBN": "978-1-59327-603-4",
		"number-of-pages": "525",
		"publisher": "No Starch Press",
		"publisher-place": "San Francisco",
		"source": "Library of Congress ISBN",
		"title": "Python crash course: a hands-on, project-based introduction to programming",
		"title-short": "Python crash course",
		"author": [
			{
				"family": "Matthes",
				"given": "Eric"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/LGXNXZZY",
		"type": "document",
		"publisher": "Humanidades Digitales Hispánicas",
		"title": "Documento de recomendaciones para la evaluación y reconocimiento de la investigación llevada a cabo en el ámbito de las humanidades digitales",
		"URL": "https://humanidadesdigitaleshispanicas.es/wp-content/uploads/2019/01/Documento_Recomendaciones_Definitivo.pdf",
		"author": [
			{
				"family": "Rodríguez Ortega",
				"given": "Nuria"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2015",
					7,
					28
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/4XZ7QQY5",
		"type": "document",
		"publisher": "Maestría en Humanidades Digitales, Universidad de los Andes",
		"title": "Valoración y clasificación de proyectos de Humanidades Digitales",
		"URL": "https://facartes.uniandes.edu.co/wp-content/uploads/2021/04/val_clasifi_proyectos_HD.pdf",
		"author": [
			{
				"family": "Afanador-Llach",
				"given": "María José"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021",
					3,
					8
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/T68SYI38",
		"type": "post-weblog",
		"abstract": "Esta guía proporciona lineamientos para ayudar a que los comités de evaluación tomen en consideración los productos digitales como resultados de investigaciones, así como orientar a los creadores de recursos digitales a los distintos elementos que deben incluir sus recursos con el objetivo de incrementar la calidad editorial de sus proyectos. La Guía además se[...]",
		"container-title": "Red de Humanidades Digitales",
		"language": "es",
		"title": "Guía de buenas prácticas para la elaboración y evaluación de proyectos de Humanidades Digitales y checklist",
		"URL": "http://humanidadesdigitales.net/guia-de-buenas-practicas-para-la-elaboracion-y-evaluacion-de-proyectos-de-humanidades-digitales-y-checklist/",
		"author": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			},
			{
				"family": "Álvarez Sánchez",
				"given": "Adriana"
			},
			{
				"family": "Barrón Tovar",
				"given": "José Francisco"
			},
			{
				"family": "Girón Palau",
				"given": "Jonathan"
			},
			{
				"family": "Peña Pimentel",
				"given": "Miriam"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					8,
					11
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020",
					5
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/EIH6C6LG",
		"type": "post-weblog",
		"language": "de-DE",
		"title": "Criteria for Reviewing Tools and Environments for Digital Scholarly Editing, version 1.0 |",
		"URL": "https://www.i-d-e.de/publikationen/weitereschriften/criteria-tools-version-1/",
		"accessed": {
			"date-parts": [
				[
					"2022",
					8,
					11
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5VJLUNG2",
		"type": "article-journal",
		"container-title": "Einreichung für den Sonderband 1 der Zeitschrift für digitale Geisteswissenschaften",
		"DOI": "10.17175/SB001_004",
		"language": "de",
		"license": "CC BY-SA 4.0",
		"note": "publisher: HAB - Herzog August Bibliothek",
		"source": "DOI.org (Datacite)",
		"title": "Digital Humanities? Gibt’s doch gar nicht!",
		"title-short": "Digital Humanities?",
		"URL": "http://zfdg.de/sb001_004",
		"author": [
			{
				"family": "Sahle",
				"given": "Patrick"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					8,
					17
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BV8HZ7HP",
		"type": "webpage",
		"abstract": "Data Summary",
		"language": "es",
		"license": "CC BY-NC-SA 4.0",
		"title": "DH Academic Trends Review",
		"URL": "https://sites.google.com/tec.mx/digitalhumanitiesacademicprodu/home",
		"author": [
			{
				"family": "Cebral-Loureda",
				"given": "Manuel"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					9,
					6
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9CK3YXYQ",
		"type": "book",
		"call-number": "AZ105 .B395 2017",
		"event-place": "Cambridge, England",
		"ISBN": "978-0-7456-9765-9",
		"number-of-pages": "189",
		"publisher": "Malden, MA : Polity",
		"publisher-place": "Cambridge, England",
		"source": "Library of Congress ISBN",
		"title": "Digital humanities: knowledge and critique in a digital age",
		"title-short": "Digital humanities",
		"editor": [
			{
				"family": "Berry",
				"given": "David M."
			},
			{
				"family": "Fagerjord",
				"given": "Anders"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ZVN7PWAE",
		"type": "chapter",
		"container-title": "Digital Humanities 2011: conference abstracts : Stanford University, Stanford, CA, USA, June 19-22, 2011",
		"event-place": "Stanford, California",
		"ISBN": "978-0-911221-47-3",
		"language": "eng",
		"note": "OCLC: 1048261449",
		"page": "vi-vii",
		"publisher": "Stanford University Library",
		"publisher-place": "Stanford, California",
		"source": "Open WorldCat",
		"title": "Welcome to the Big Tent",
		"author": [
			{
				"family": "Jockers",
				"given": "Matthew Lee"
			},
			{
				"family": "Worthey",
				"given": "Glen"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2011"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RJQEZQH6",
		"type": "book",
		"event-place": "Stanford, California",
		"ISBN": "978-0-911221-47-3",
		"language": "eng",
		"note": "OCLC: 1048261449",
		"publisher": "Stanford University Library",
		"publisher-place": "Stanford, California",
		"source": "Open WorldCat",
		"title": "Digital Humanities 2011: conference abstracts : Stanford University, Stanford, CA, USA, June 19-22, 2011",
		"title-short": "Digital Humanities 2011",
		"issued": {
			"date-parts": [
				[
					"2011"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/SVIVWDXD",
		"type": "webpage",
		"language": "en",
		"title": "The Digital Humanities Manifesto 2.0",
		"URL": "https://www.digitalmanifesto.net/manifestos/17/",
		"author": [
			{
				"family": "Schnapp",
				"given": "Jeffrey"
			},
			{
				"family": "Lunenfeld",
				"given": "Peter"
			},
			{
				"family": "Presner",
				"given": "Todd"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					9,
					6
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2008"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/FT72DGNC",
		"type": "article-journal",
		"abstract": "Defining digital humanities might be an endless debate if we stick to the discussion about the boundaries of this concept as an academic “discipline”. In an attempt to concretely identify this field and its actors, this paper shows that it is possible to analyse them through Twitter, a social media widely used by this “community of practice”. Based on a network analysis of 2,500 users identified as members of this movement, the visualisation of the “who’s following who?” graph allows us to highlight the structure of the network’s relationships, and identify users whose position is particular. Specifically, we show that linguistic groups are key factors to explain clustering within a network whose characteristics look similar to a small world.",
		"container-title": "Cogent Arts & Humanities",
		"DOI": "10.1080/23311983.2016.1171458",
		"ISSN": "null",
		"issue": "1",
		"note": "publisher: Cogent OA\n_eprint: https://doi.org/10.1080/23311983.2016.1171458",
		"page": "1171458",
		"source": "Taylor and Francis+NEJM",
		"title": "A social network analysis of Twitter: Mapping the digital humanities community",
		"title-short": "A social network analysis of Twitter",
		"URL": "https://doi.org/10.1080/23311983.2016.1171458",
		"volume": "3",
		"author": [
			{
				"family": "Grandjean",
				"given": "Martin"
			}
		],
		"editor": [
			{
				"family": "Mauro",
				"given": "Aaron"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					9,
					29
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016",
					12,
					31
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QV5HR3P9",
		"type": "article-newspaper",
		"abstract": "Computer science reduces the world to numbers. The humanities teach us how much those numbers fail to capture. Perhaps if computer scientists looked up from their screens of code they might understand why the humanities are ever more important in a world increasingly defined by code.",
		"container-title": "Forbes",
		"language": "en",
		"section": "AI & Big Data",
		"title": "Why Computer Science Needs The Humanities",
		"URL": "https://www.forbes.com/sites/kalevleetaru/2019/08/06/why-computer-science-needs-the-humanities/",
		"author": [
			{
				"family": "Leetaru",
				"given": "Kalev"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					9,
					29
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2019",
					8,
					6
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/B6DUFHVK",
		"type": "book",
		"abstract": "\"Exploratory Programming for the Arts and Humanities offers a course on programming without prerequisites. It covers both the essentials of computing and the main areas in which computing applies to the arts and humanities\"--",
		"call-number": "QA76.6 .M664 2021",
		"edition": "Second edition",
		"event-place": "Cambridge, Massachusetts",
		"ISBN": "978-0-262-04460-8",
		"number-of-pages": "363",
		"publisher": "The MIT Press",
		"publisher-place": "Cambridge, Massachusetts",
		"source": "Library of Congress ISBN",
		"title": "Exploratory programming for the arts and humanities",
		"author": [
			{
				"family": "Montfort",
				"given": "Nick"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5IV6QDNC",
		"type": "article-journal",
		"abstract": "This article presents a selection of findings from a survey-based study on the role of software development and programming in the Digital Humanities, disseminated to researchers, teachers, and practitioners from across the community.",
		"container-title": "Digital Scholarship in the Humanities",
		"DOI": "10.1093/llc/fqv042",
		"ISSN": "2055-7671",
		"issue": "suppl_1",
		"journalAbbreviation": "Digital Scholarship in the Humanities",
		"page": "i142-i147",
		"source": "Silverchair",
		"title": "Programming in the Digital Humanities",
		"URL": "https://doi.org/10.1093/llc/fqv042",
		"volume": "30",
		"author": [
			{
				"family": "O’Sullivan",
				"given": "James"
			},
			{
				"family": "Jakacki",
				"given": "Diane"
			},
			{
				"family": "Galvin",
				"given": "Mary"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					9,
					29
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015",
					12,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RAH93FN9",
		"type": "article-journal",
		"abstract": "Digital literacy is among the mandatory abilities to any higher education level and represents a fundamental ingredient in successful professionalization. Considering the deep penetration of digital technologies in everyday life, digital literacy offers a set of transversal skills that could improve a whole area of activities, from banking operations to civic participation. However, these skills are diverse and vary according to the development of technologies and society. This study fills an important academic gap on digital literacy by placing it in a specific and well-defined context, analyzing different perspectives that involve such learning, such as predictors of digital literacy in different types of students. In addition, research increases its importance as it is being developed during the pandemic, a period characterized by accelerated technological use and sudden changes. This research used a quantitative design based on the answers to a questionnaire conducted from March 2021 to May 2021. From a methodological perspective, we tested several hypotheses using one-way analysis of variance (ANOVA) and confirmatory factor analysis (CFA) within the structural equation model (SEM). The results show that communication, critical thinking, problem-solving, and technical digital skills are more present in the case of students enrolled in social sciences, while other digital skills (i.e., creativity and information) are more prevalent in the case of humanities students. Moreover, the results showed that, except for creativity and problem-solving-related digital skills, all of the digital skills were significantly influenced by students’ different levels of education.",
		"container-title": "Sustainability",
		"DOI": "10.3390/su14052483",
		"ISSN": "2071-1050",
		"issue": "5",
		"language": "en",
		"license": "http://creativecommons.org/licenses/by/3.0/",
		"note": "number: 5\npublisher: Multidisciplinary Digital Publishing Institute",
		"page": "2483",
		"source": "www.mdpi.com",
		"title": "Exploring Digital Literacy Skills in Social Sciences and Humanities Students",
		"URL": "https://www.mdpi.com/2071-1050/14/5/2483",
		"volume": "14",
		"author": [
			{
				"family": "Vodă",
				"given": "Ana Iolanda"
			},
			{
				"family": "Cautisanu",
				"given": "Cristina"
			},
			{
				"family": "Grădinaru",
				"given": "Camelia"
			},
			{
				"family": "Tănăsescu",
				"given": "Chris"
			},
			{
				"family": "Moraes",
				"given": "Gustavo Herminio Salati Marcondes",
				"non-dropping-particle": "de"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					10,
					25
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022",
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/GJZ5ZABZ",
		"type": "post-weblog",
		"abstract": "Por las responsabilidades que actualmente tengo en la Facultad de Filosofía y Letras de la UNAM, intervengo en las decisiones de adquisición, asignación y organización de la red de cómputo. Justo en estos días participo en la elaboración de la solicitud al Consejo Asesor de Tecnologías de la Información, para cubrir las necesidades de la[...]",
		"container-title": "Red de Humanidades Digitales",
		"language": "es",
		"title": "¿Infraestructura de cómputo para las humanidades?",
		"URL": "http://humanidadesdigitales.net/infraestructura-de-computo-para-las-humanidades/",
		"author": [
			{
				"family": "Priani",
				"given": "Ernesto"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					10,
					25
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2012",
					3,
					10
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WCFKMUIZ",
		"type": "chapter",
		"collection-title": "Routledge international handbooks",
		"container-title": "Routledge international handbook of research methods in digital humanities",
		"event-place": "London New York",
		"ISBN": "978-1-138-36302-1",
		"language": "eng",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London New York",
		"source": "K10plus ISBN",
		"title": "Opening the ‘black box’ of digital cultural heritage processes",
		"URL": "https://www.routledge.com/9781138363021",
		"editor": [
			{
				"family": "Schuster",
				"given": "Kristen"
			},
			{
				"family": "Dunn",
				"given": "Stuart E."
			}
		],
		"author": [
			{
				"family": "Smyth",
				"given": "Hannah"
			},
			{
				"family": "Nyhan",
				"given": "Julianne"
			},
			{
				"family": "Flinn",
				"given": "Andrew"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/UXKBXC48",
		"type": "book",
		"collection-title": "Routledge international handbooks",
		"event-place": "London New York",
		"ISBN": "978-1-138-36302-1",
		"language": "eng",
		"number-of-pages": "472",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London New York",
		"source": "K10plus ISBN",
		"title": "Routledge international handbook of research methods in digital humanities",
		"editor": [
			{
				"family": "Schuster",
				"given": "Kristen"
			},
			{
				"family": "Dunn",
				"given": "Stuart E."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QSBRTWNK",
		"type": "article-journal",
		"abstract": "This article proposes that the practice of information visualisation (infovis), from its beginnings in the second part of the eighteenth century until today, relied on two key principles. The first principle is reduction. Infovis uses graphical primitives such as points, straight lines, curves and simple geometric shapes to stand in for objects and relations between them. The second principle is the use of spatial variables (position, size, shape and, more recently, movement) to represent key differences in the data and reveal patterns and relations. Following this analysis, the author discusses a more recent visualisation method which we can call ‘direct visualisation’ (or ‘media visualisation’): creating new visual representations from the actual visual media objects (images, video) or their parts. The article analyses the well-known examples of artistic visualisations that use this method: Listening Post (Ben Rubin and Mark Hansen), Cinema Redux (Brendan Dawes) and Preservation of Selected Traces (Ben Fry). It further suggests that direct visualisation is particularly relevant for humanities, media studies and cultural institutions. Using the actual visual artefacts in visualisation as opposed to representing them by graphical primitives helps the researcher to understand meaning and/or cause behind the patterns she may observe, as well as to discover additional patterns. To illustrate this idea, examples of projects created in the author's lab at UCSD (softwarestudies.com) are presented. Founded in 2007, the lab works on techniques and software to allow interactive exploration of large sets of visual cultural data using a direct visualisation approach and supervisualisation systems such as 215 megapixel HIPerSpace. The examples of its work are visualisations of 4553 covers of every issue of Time magazine published between 1923 and 2009; visualisations of all pages of every issue of Science and Popular Science magazines published between 1872 and 1922; and a set of visualisations of 1 million pages on Manga series.",
		"container-title": "Visual Studies",
		"DOI": "10.1080/1472586X.2011.548488",
		"ISSN": "1472-586X",
		"issue": "1",
		"note": "publisher: Routledge\n_eprint: https://doi.org/10.1080/1472586X.2011.548488",
		"page": "36-49",
		"source": "Taylor and Francis+NEJM",
		"title": "What is visualization?",
		"URL": "https://doi.org/10.1080/1472586X.2011.548488",
		"volume": "26",
		"author": [
			{
				"family": "Manovich",
				"given": "Lev"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					11,
					29
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2011",
					3,
					15
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VBY8JYET",
		"type": "article-journal",
		"title": "Digitization of library resources: Challenges and implications for policy and planning",
		"author": [
			{
				"family": "Fabunmi",
				"given": "Beatrice Ayodeji"
			},
			{
				"family": "Paris",
				"given": "Matthew"
			},
			{
				"family": "Fabunmi",
				"given": "Martins"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2006"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VKPCD53Y",
		"type": "article-journal",
		"container-title": "Online Information Review",
		"note": "ISBN: 1468-4527\npublisher: Emerald Group Publishing Limited",
		"title": "Best practices, standards and techniques for digitizing library materials: a snapshot of library digitization practices in the USA",
		"author": [
			{
				"family": "Liu",
				"given": "Yan Quan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2004"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/YCRDG7L5",
		"type": "article-journal",
		"container-title": "Library hi tech",
		"note": "ISBN: 0737-8831\npublisher: Emerald Group Publishing Limited",
		"title": "Library digitization projects, issues and guidelines: A survey of the literature",
		"author": [
			{
				"family": "Lopatin",
				"given": "Laurie"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2006"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ESPJK3K8",
		"type": "article-journal",
		"container-title": "Journal of Web Librarianship",
		"issue": "4",
		"note": "ISBN: 1932-2909\npublisher: Taylor & Francis",
		"page": "384-403",
		"title": "Assessment of digitized library and archives materials: A literature review",
		"volume": "8",
		"author": [
			{
				"family": "Kelly",
				"given": "Elizabeth Joan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2014"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/KNZW4VZZ",
		"type": "article-journal",
		"container-title": "International Journal of Information Dissemination and Technology",
		"issue": "4",
		"page": "228-231",
		"title": "Digital library and digitization",
		"volume": "1",
		"author": [
			{
				"family": "Maurya",
				"given": "Ram Nath"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2011"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/G4WDC22Z",
		"type": "paper-conference",
		"container-title": "ADHO 2017-Montréal",
		"title": "Access to cultural heritage data: a challenge for the Digital Humanities",
		"author": [
			{
				"family": "Baillot",
				"given": "Anne"
			},
			{
				"family": "Puren",
				"given": "Marie"
			},
			{
				"family": "Riondet",
				"given": "Charles"
			},
			{
				"family": "Romary",
				"given": "Laurent"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7FFYGKCL",
		"type": "article-journal",
		"container-title": "The Bloomsbury Handbook to the Digital Humanities",
		"note": "ISBN: 1350232122\npublisher: Bloomsbury Publishing",
		"page": "255",
		"title": "Digital Humanities and Digitized Cultural Heritage",
		"author": [
			{
				"family": "Terras",
				"given": "Melissa"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/SIKZI2AJ",
		"type": "chapter",
		"container-title": "The Bloomsbury Handbook to the Digital Humanities",
		"event-place": "New York",
		"ISBN": "1-350-23212-2",
		"note": "ISBN: 1350232122\npublisher: Bloomsbury Publishing",
		"page": "41-48",
		"publisher": "Bloomsbury Academic",
		"publisher-place": "New York",
		"title": "Postcolonial Digital Humanities Reconsidered",
		"author": [
			{
				"family": "Risam",
				"given": "Roopika"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/IUFW44RB",
		"type": "chapter",
		"container-title": "The Bloomsbury Handbook to the Digital Humanities",
		"event-place": "New York",
		"ISBN": "1-350-23212-2",
		"note": "ISBN: 1350232122\npublisher: Bloomsbury Publishing",
		"page": "83-92",
		"publisher": "Bloomsbury Academic",
		"publisher-place": "New York",
		"title": "Multilingual digital humanities",
		"author": [
			{
				"family": "Nilsson-Fernández",
				"given": "Pedro"
			},
			{
				"family": "Dombrowski",
				"given": "Quinn"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9P6V8V5H",
		"type": "article-journal",
		"abstract": "This article proposes a Digital Humanities research methodology in colonial literature, namely late fifteenth and early sixteen century Spanish colonial literature, in order to explore the possibilities of Digital Media in the literature classroom. After an introduction to the software Antconc developed by Professor Laurence Anthony and explanation of its usages, the article analyses two epistolary texts from Hernán Cortés and Christopher Columbus through a correlative linguistic and terminology approach. The conclusions show how these conquistadors manipulate language related to space in order to reach their goal of colonizing the so-called New World, pledging to \"civilize\" the territory and its inhabitants. Ultimately, this article draws on alternative pedagogical methodologies and tools that can contribute immensely to the literature classroom in the COVID-19 era, a time that calls for educative renovation and the development of teaching strategies for the online, not in-person instruction. The methodology and its analysis exemplify the possibilities of Digital Humanities to offer new, interesting approaches to colonial literature through spatial theory.",
		"container-title": "The International Journal of Humanities Education",
		"DOI": "10.18848/2327-0063/CGP/v20i01/53-66",
		"ISSN": "23270063",
		"issue": "1",
		"language": "English",
		"license": "Copyright © 2022, Common Ground Research Networks, All Rights Reserved",
		"note": "number-of-pages: 53-66\npublisher-place: Madrid, United States\npublisher: Common Ground Research Networks",
		"page": "53-66",
		"source": "ProQuest",
		"title": "Digital Humanities and Colonial Literature: The Reinvention of Space",
		"title-short": "Digital Humanities and Colonial Literature",
		"URL": "https://www.proquest.com/docview/2743806207/abstract/C887FFDC2F0E46CCPQ/1",
		"volume": "20",
		"author": [
			{
				"family": "Gutiérrez",
				"given": "Judit Palencia"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					13
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/3XAST7WI",
		"type": "article-journal",
		"abstract": "This article serves as the introduction to DHQ's Special Issue, \"Imagining the DH Undergraduate: Special Issue in Undergraduate Education in DH.\" Co-editors Emily Christina Murphy and Shannon R. Smith introduce the issue–its signficance, theoretical underpinnings, structure, articles, and case studies. The special issue is organized into four thematic clusters: 1) program models; 2) disciplinarity and DH pedagogy; 3) tool development; and 4) professional concerns.",
		"container-title": "Digital Humanities Quarterly",
		"ISSN": "1938-4122",
		"issue": "3",
		"journalAbbreviation": "DHQ",
		"title": "Introduction",
		"URL": "http://digitalhumanities.org:8081/dhq/vol/11/3/000334/000334.html",
		"volume": "011",
		"author": [
			{
				"family": "Murphy",
				"given": "Emily Christina"
			},
			{
				"family": "Smith",
				"given": "Shannon R."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017",
					10,
					2
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ZV9YLW2H",
		"type": "article-journal",
		"abstract": "This case study describes two iterations of a Digital Humanities (DH) “Studio” course on scholarly text encoding as a model for a DH curriculum at a small liberal arts college. Designed to accompany a three-credit humanities course, the one-credit DH Studios are taught by library faculty. The paired courses share a final project—a digital edition of a short work of literature encoded in the Text Encoding Initiative. The DH Studio creates a methodology-focused environment for students to practice information and digital literacies.",
		"container-title": "College & Undergraduate Libraries",
		"DOI": "10.1080/10691316.2017.1326331",
		"ISSN": "1069-1316",
		"issue": "2-4",
		"note": "publisher: Routledge\n_eprint: https://doi.org/10.1080/10691316.2017.1326331",
		"page": "467-481",
		"source": "Taylor and Francis+NEJM",
		"title": "Teaching TEI to undergraduates: A case study in a digital humanities curriculum",
		"title-short": "Teaching TEI to undergraduates",
		"URL": "https://doi.org/10.1080/10691316.2017.1326331",
		"volume": "24",
		"author": [
			{
				"family": "Brooks",
				"given": "Mackenzie"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					14
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2017",
					10,
					2
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Y8AVH5BX",
		"type": "chapter",
		"abstract": "In late summer of 2010, I arrived on the campus of St. Norbert College in De Pere, Wisconsin. I was a newly minted assistant professor, brimming with optimism, and the field with which I increasingly identified my work—this “digital humanities”—had just been declared “the first ‘next big thing’ in a long time” by William Pannapacker in his  <i>Chronicle of Higher Education</i>  column.¹ “We are now realizing,” Pannapacker had written of the professors gathered at the Modern Language Association’s annual convention, “that resistance is futile” (“MLA and the Digital Humanities”). So of course I immediately proposed a new “Introduction",
		"container-title": "Debates in the Digital Humanities 2016",
		"ISBN": "978-0-8166-9954-4",
		"note": "DOI: 10.5749/j.ctt1cn6thb.39",
		"page": "459-474",
		"publisher": "University of Minnesota Press",
		"source": "JSTOR",
		"title": "How Not to Teach Digital Humanities",
		"URL": "https://www.jstor.org/stable/10.5749/j.ctt1cn6thb.39",
		"author": [
			{
				"family": "Cordell",
				"given": "Ryan"
			}
		],
		"editor": [
			{
				"family": "Gold",
				"given": "Matthew K."
			},
			{
				"family": "Klein",
				"given": "Lauren F."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					14
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6PLN7FJL",
		"type": "chapter",
		"container-title": "Digital humanities pedagogy: Practices, principles and politics",
		"event-place": "Cambridge",
		"ISBN": "1-909254-25-8",
		"page": "3-30",
		"publisher": "Open Book Publishers",
		"publisher-place": "Cambridge",
		"title": "</Parentheses>: Digital Humanities and the Place of Pedagogy",
		"volume": "3",
		"editor": [
			{
				"family": "Hirsch",
				"given": "Brett D."
			}
		],
		"author": [
			{
				"family": "Hirsch",
				"given": "Brett D."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/TF8CT5XY",
		"type": "book",
		"event-place": "Cambridge",
		"ISBN": "1-909254-25-8",
		"number-of-pages": "426",
		"publisher": "Open Book Publishers",
		"publisher-place": "Cambridge",
		"title": "Digital humanities pedagogy: Practices, principles and politics",
		"volume": "3",
		"editor": [
			{
				"family": "Hirsch",
				"given": "Brett D."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2012"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/UY5RKDXT",
		"type": "article-journal",
		"container-title": "Index. comunicación: Revista científica en el ámbito de la Comunicación Aplicada",
		"issue": "2",
		"note": "ISBN: 2174-1859\npublisher: Departamento de Comunicación I",
		"page": "13-31",
		"title": "El rol del docente universitario y su implicación ante las humanidades digitales",
		"volume": "8",
		"author": [
			{
				"family": "Cano",
				"given": "Daniel Rodrigo"
			},
			{
				"family": "Casas Moreno",
				"given": "Patricia",
				"non-dropping-particle": "de"
			},
			{
				"family": "Gómez",
				"given": "José Ignacio Aguaded"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/VSTFZTLE",
		"type": "paper-conference",
		"container-title": "Humanidades Digitales: Construcciones locales en contextos globales: Actas del I Congreso Internacional de la Asociación Argentina de Humanidades Digitales-AAHD",
		"ISBN": "987-40-1997-2",
		"page": "22",
		"publisher": "Facultad de Filosofía y Letras-Instituto de Geografía",
		"title": "Enseñar edición digital con TEI en español. Aprendizaje situado y transculturación",
		"author": [
			{
				"family": "Torrent",
				"given": "Susanna Allés"
			},
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/X5CHBNVC",
		"type": "paper-conference",
		"container-title": "III Congreso de la Sociedad Internacional Humanidades Digitales Hispánicas Sociedades, políticas, saberes (Libro de resúmenes)",
		"note": "issue: 20",
		"page": "287",
		"title": "Las Humanidades Digitales como una plataforma de aprendizaje para enseñar entre España y Latinoamérica",
		"volume": "18",
		"author": [
			{
				"family": "González-Blanco",
				"given": "Elena"
			},
			{
				"family": "Rio Riande",
				"given": "Gimena",
				"non-dropping-particle": "del"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/NKI28I9H",
		"type": "book",
		"publisher": "University of Michigan Press",
		"title": "Hacking the academy: New approaches to scholarship and teaching from digital humanities",
		"author": [
			{
				"family": "Cohen",
				"given": "Daniel J."
			},
			{
				"family": "Scheinfeldt",
				"given": "Tom"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2013"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7PDJTLHM",
		"type": "article-journal",
		"container-title": "Debates in the digital humanities",
		"note": "publisher: JSTOR",
		"page": "459-74",
		"title": "How not to teach digital humanities",
		"author": [
			{
				"family": "Cordell",
				"given": "Ryan"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/72PIDPDB",
		"type": "chapter",
		"call-number": "AZ105 .A35 2014",
		"container-title": "Doing digital humanities: practice, training, research",
		"event-place": "New York, NY",
		"ISBN": "978-1-138-89943-8",
		"publisher": "Routledge",
		"publisher-place": "New York, NY",
		"source": "Library of Congress ISBN",
		"title": "Dissemination as Cultivation: Scholarly Communications in a Digital Age",
		"editor": [
			{
				"family": "Crompton",
				"given": "Constance"
			},
			{
				"family": "Lane",
				"given": "Richard J."
			},
			{
				"family": "Siemens",
				"given": "Raymond George"
			}
		],
		"author": [
			{
				"family": "O'Sullivan",
				"given": "James"
			},
			{
				"family": "Long",
				"given": "Christopher P."
			},
			{
				"family": "Mattson",
				"given": "Mark"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9NLEY4PT",
		"type": "chapter",
		"container-title": "The Bloomsbury Handbook to the Digital Humanities",
		"event-place": "Londres",
		"note": "ISBN: 1350232122\npublisher: Bloomsbury Publishing",
		"page": "445-458",
		"publisher": "Bloomsbury Publishing",
		"publisher-place": "Londres",
		"title": "AI, Ethics, and Digital Humanities",
		"author": [
			{
				"family": "Berry",
				"given": "David M."
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/9F8Q4IYH",
		"type": "article-journal",
		"abstract": "The digital transformation is turning archives, both old and new, into data. As a consequence, automation in the form of artificial intelligence techniques is increasingly applied both to scale traditional recordkeeping activities, and to experiment with novel ways to capture, organise, and access records. We survey recent developments at the intersection of Artificial Intelligence and archival thinking and practice. Our overview of this growing body of literature is organised through the lenses of the Records Continuum model. We find four broad themes in the literature on archives and artificial intelligence: theoretical and professional considerations, the automation of recordkeeping processes, organising and accessing archives, and novel forms of digital archives. We conclude by underlining emerging trends and directions for future work, which include the application of recordkeeping principles to the very data and processes that power modern artificial intelligence and a more structural—yet critically aware—integration of artificial intelligence into archival systems and practice.",
		"container-title": "Journal on Computing and Cultural Heritage",
		"DOI": "10.1145/3479010",
		"ISSN": "1556-4673",
		"issue": "1",
		"journalAbbreviation": "J. Comput. Cult. Herit.",
		"page": "4:1–4:15",
		"source": "February 2022",
		"title": "Archives and AI: An Overview of Current Debates and Future Perspectives",
		"title-short": "Archives and AI",
		"URL": "https://doi.org/10.1145/3479010",
		"volume": "15",
		"author": [
			{
				"family": "Colavizza",
				"given": "Giovanni"
			},
			{
				"family": "Blanke",
				"given": "Tobias"
			},
			{
				"family": "Jeurgens",
				"given": "Charles"
			},
			{
				"family": "Noordegraaf",
				"given": "Julia"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					14
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2021",
					12,
					14
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/Z5U8VMPN",
		"type": "article-journal",
		"container-title": "A companion to digital humanities",
		"note": "publisher: Blackwell",
		"page": "288-290",
		"title": "The digital humanities and humanities computing: An introduction",
		"author": [
			{
				"family": "Schreibman",
				"given": "Susan"
			},
			{
				"family": "Siemens",
				"given": "Ray"
			},
			{
				"family": "Unsworth",
				"given": "John"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2004"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/I9YNAC8B",
		"type": "article-journal",
		"container-title": "Journal of data and information science",
		"issue": "1",
		"note": "ISBN: 2096-157X",
		"page": "1-12",
		"title": "Smart data for digital humanities",
		"volume": "2",
		"author": [
			{
				"family": "Zeng",
				"given": "Marcia Lei"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/IDKJM79Q",
		"type": "chapter",
		"collection-title": "Digital Humanities Research",
		"container-title": "Digital Methods in the Humanities: Challenges, Ideas, Perspectives",
		"edition": "1",
		"event-place": "Bielefeld, Germany",
		"ISBN": "978-3-8376-5419-6",
		"language": "en",
		"note": "DOI: 10.14361/9783839454190",
		"publisher": "Bielefeld University Press / transcript Verlag",
		"publisher-place": "Bielefeld, Germany",
		"source": "DOI.org (Crossref)",
		"title": "From text to data. Digitization, text analysis and corpus linguistics",
		"URL": "https://www.transcript-open.de/isbn/5419",
		"volume": "1",
		"editor": [
			{
				"family": "Schwandt",
				"given": "Silke"
			}
		],
		"author": [
			{
				"family": "Jentsch",
				"given": "Patrick"
			},
			{
				"family": "Parada",
				"given": "Setephan"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					14
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/U65X4V5U",
		"type": "book",
		"abstract": "Digital Humanities is a transformational endeavor that not only changes the perception, storage, and interpretation of information but also of research processes and questions. It also prompts new ways of interdisciplinary communication between humanities scholars and computer scientists.  This volume offers a unique perspective on digital methods for and in the humanities. It comprises case studies from various fields to illustrate the challenge of matching existing textual research practices and digital tools. Problems and solutions with and for training tools as well as the adjustment of research practices are presented and discussed with an interdisciplinary focus.",
		"collection-title": "Digital Humanities Research",
		"edition": "1",
		"event-place": "Bielefeld, Germany",
		"ISBN": "978-3-8376-5419-6",
		"language": "en",
		"note": "DOI: 10.14361/9783839454190",
		"publisher": "Bielefeld University Press / transcript Verlag",
		"publisher-place": "Bielefeld, Germany",
		"source": "DOI.org (Crossref)",
		"title": "Digital Methods in the Humanities: Challenges, Ideas, Perspectives",
		"title-short": "Digital Methods in the Humanities",
		"URL": "https://www.transcript-open.de/isbn/5419",
		"volume": "1",
		"editor": [
			{
				"family": "Schwandt",
				"given": "Silke"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					14
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/BFNHCBNS",
		"type": "article-journal",
		"abstract": "This article provides a critical review of the past five years of literature in digital humanities pedagogy and faculty-librarian collaboration, commingled with reflections on personal practice, which extend findings from the literature. Faculty-librarian partnerships in DH pedagogy reflect a rapidly evolving area of engagement calling for expertise in teaching, subject knowledge, scholarly communication, digital technologies, and DH research methodologies. Although there is a rapidly expanding body of literature on these partnerships, the challenges of the work tend to be minimized. This article expands upon commonly encountered difficulties, and it points to potential solutions and best practices.",
		"container-title": "College & Undergraduate Libraries",
		"DOI": "10.1080/10691316.2017.1340217",
		"ISSN": "1069-1316",
		"issue": "2-4",
		"note": "publisher: Routledge\n_eprint: https://doi.org/10.1080/10691316.2017.1340217",
		"page": "257-269",
		"source": "Taylor and Francis+NEJM",
		"title": "Against the grain: Reading for the challenges of collaborative digital humanities pedagogy",
		"title-short": "Against the grain",
		"URL": "https://doi.org/10.1080/10691316.2017.1340217",
		"volume": "24",
		"author": [
			{
				"family": "Giannetti",
				"given": "Francesca"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					15
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2017",
					10,
					2
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6C9I5U66",
		"type": "article-journal",
		"container-title": "CEA Critic",
		"DOI": "10.1353/cea.2014.0015",
		"ISSN": "2327-5898",
		"issue": "2",
		"note": "publisher: Johns Hopkins University Press",
		"page": "140-146",
		"source": "Project MUSE",
		"title": "Introducing Digital Humanities Pedagogy",
		"URL": "https://muse.jhu.edu/pub/1/article/550518",
		"volume": "76",
		"author": [
			{
				"family": "Iantorno",
				"given": "Luke A."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2022",
					12,
					15
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2014"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/A8QU6MGU",
		"type": "report",
		"event-place": "St Charles, Missouri",
		"genre": "White paper",
		"publisher": "Universidad de Lindenwood",
		"publisher-place": "St Charles, Missouri",
		"title": "Improving Digital Humanities Pedagogy in St. Louis",
		"URL": "https://digitalcommons.lindenwood.edu/mhc_grant.pdf",
		"author": [
			{
				"family": "Carnes",
				"given": "Geremy"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022",
					6,
					24
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/ITFE2CWF",
		"type": "book",
		"abstract": "\"The Bloomsbury Handbook to the Digital Humanities reconsiders key debates, methods, possibilities, and failings from across the digital humanities, offering a timely interrogation of the present and future of the arts and humanities in the digital age. Comprising 43 essays from some of the field's leading scholars and practitioners, this comprehensive collection examines, among its many subjects, the emergence and ongoing development of DH, postcolonial digital humanities, feminist digital humanities, race and DH, multilingual digital humanities, media studies as DH, the failings of DH, critical digital humanities, the future of text encoding, cultural analytics, natural language processing, open access and digital publishing, digital cultural heritage, archiving and editing, sustainability, DH pedagogy, labour, artificial intelligence, the cultural economy, and the role of the digital humanities in climate change. The Bloomsbury Handbook to the Digital Humanities: Surveys key contemporary debates within DH, focusing on pressing issues of perspective, methodology, access, capacity, and sustainability. Reconsiders and reimagines the past, present, and future of the digital humanities. Features an intuitive structure which divides topics across five sections: \"Perspectives & Polemics\", \"Methods, Tools & Techniques\", \"Public Digital Humanities\", \"Institutional Contexts\", and \"DH Futures\". Comprehensive in scope and accessibility written, this book is essential reading for students, scholars, and practitioners working across the digital humanities and wider arts and humanities. Featuring contributions from pre-eminent scholars and radical thinkers both established and emerging, The Bloomsbury Handbook to the Digital Humanities should long serve as a roadmap through the myriad formulations, methodologies, opportunities, and limitations of DH. Comprehensive in its scope, pithy in style yet forensic in its scholarship, this book is essential reading for students, scholars, and practitioners working across the digital humanities, whatever DH might be, and whatever DH might become\"--",
		"collection-title": "Bloomsbury Handbooks",
		"event-place": "New York",
		"ISBN": "978-1-350-23211-2",
		"publisher": "Bloomsbury Academic",
		"publisher-place": "New York",
		"source": "Library of Congress ISBN",
		"title": "The Bloomsbury Handbook to the Digital Humanities",
		"editor": [
			{
				"family": "O'Sullivan",
				"given": "James"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/SKQQJSR7",
		"type": "book",
		"edition": "Second edition",
		"event-place": "London New York Oxford New Delhi Sydney",
		"ISBN": "978-1-350-18089-5",
		"language": "eng",
		"number-of-pages": "257",
		"publisher": "Bloomsbury Academic",
		"publisher-place": "London New York Oxford New Delhi Sydney",
		"source": "K10plus ISBN",
		"title": "Using digital humanities in the classroom: a practical introduction for teachers, lecturers, and students",
		"title-short": "Using digital humanities in the classroom",
		"author": [
			{
				"family": "Battershill",
				"given": "Claire"
			},
			{
				"family": "Ross",
				"given": "Shawna"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6XC7TSTD",
		"type": "book",
		"collection-number": "1",
		"collection-title": "Biblioteca de Humanidades Digitales",
		"event-place": "Ciudad de México",
		"ISBN": "978-607-8560-59-2",
		"language": "es",
		"note": "OCLC: 1311091717",
		"publisher": "Bonilla Artigas",
		"publisher-place": "Ciudad de México",
		"source": "Open WorldCat",
		"title": "Humanidades Digitales: recepción, institucionalización y crítica",
		"title-short": "Humanidades Digitales",
		"editor": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			},
			{
				"family": "Peña Pimentel",
				"given": "Miriam"
			},
			{
				"family": "Priani",
				"given": "Ernesto"
			},
			{
				"family": "Barrón Tovar",
				"given": "José Francisco"
			},
			{
				"family": "Domínguez Herbón",
				"given": "David"
			},
			{
				"family": "Álvarez Sánchez",
				"given": "Adriana"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WZ7NQ9NK",
		"type": "chapter",
		"collection-number": "1",
		"collection-title": "Biblioteca de Humanidades Digitales",
		"container-title": "Humanidades Digitales: recepción, institucionalización y crítica",
		"event-place": "Ciudad de México",
		"ISBN": "978-607-8560-59-2",
		"language": "es",
		"note": "OCLC: 1311091717",
		"page": "82-121",
		"publisher": "Bonilla Artigas",
		"publisher-place": "Ciudad de México",
		"source": "Open WorldCat",
		"title": "Aprender en el marco de las Ciencias Sociales y las Humanidades Digitales",
		"editor": [
			{
				"family": "Galina Russell",
				"given": "Isabel"
			},
			{
				"family": "Peña Pimentel",
				"given": "Miriam"
			},
			{
				"family": "Priani",
				"given": "Ernesto"
			},
			{
				"family": "Barrón Tovar",
				"given": "José Francisco"
			},
			{
				"family": "Domínguez Herbón",
				"given": "David"
			},
			{
				"family": "Álvarez Sánchez",
				"given": "Adriana"
			}
		],
		"author": [
			{
				"family": "Romero-Frías",
				"given": "Esteban"
			},
			{
				"family": "Suárez Guerrero",
				"given": "Cristóbal"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/PJS35NGT",
		"type": "chapter",
		"call-number": "P96.N35 D38 2018",
		"collection-title": "A K Peters Visualization Series",
		"container-title": "Data-driven storytelling",
		"event-place": "Boca Raton, Florida",
		"ISBN": "978-1-138-19710-7",
		"page": "17-58",
		"publisher": "CRC Press/Taylor & Francis Group",
		"publisher-place": "Boca Raton, Florida",
		"source": "Library of Congress ISBN",
		"title": "Storytelling in the Wild: Implications for Data Storytelling",
		"editor": [
			{
				"family": "Riche",
				"given": "Nathalie Henry"
			},
			{
				"family": "Hurter",
				"given": "Christophe"
			},
			{
				"family": "Diakopoulos",
				"given": "Nicholas"
			},
			{
				"family": "Carpendale",
				"given": "Sheelagh"
			}
		],
		"author": [
			{
				"family": "Tversky",
				"given": "Barbara"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/6YDQ7234",
		"type": "article-journal",
		"container-title": "Revista EducaOnline",
		"issue": "2",
		"language": "pr",
		"page": "5-26",
		"title": "Ensinar Humanidades Digitais sem as Humanidades Digitais: um olhar a partir das licenciaturas em História",
		"URL": "https://revistaeducaonline.eba.ufrj.br/edi%C3%A7%C3%B5es-anteriores/2021-2/ensinar-humanidades-digitais-sem-as-humanidades-digitais-um-olhar-a-partir",
		"volume": "15",
		"author": [
			{
				"family": "Alves",
				"given": "Daniel"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2021"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7YC4R56C",
		"type": "paper-conference",
		"event-place": "Montevideo",
		"event-title": "Jornadas de Investigación FIC",
		"language": "es",
		"note": "Resúmenes: https://ji.fic.edu.uy/30_-noviembre-1800-2000-h/",
		"publisher-place": "Montevideo",
		"source": "Zotero",
		"title": "Las Humanidades Digitales en el contexto latinoamericano",
		"URL": "https://ji.fic.edu.uy/wp-content/uploads/2018/07/GT3_Las-Humanidades-Digitales-en-el-contexto-latinoamericano.pdf",
		"author": [
			{
				"family": "Ezquerra",
				"given": "Carlos"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2017",
					11,
					30
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/MVNFC7Y6",
		"type": "article-journal",
		"abstract": "The Text Encoding Initiative (TEI)1 has provided a complex and comprehensive system of provisions for scholarly text encoding. Although a major focus of the\n‘digital humanities’ domain, and despite much teaching effort by the TEI community, there is a lack of teaching materials\navailable, which would encourage the adoption of the TEI's recommendations and the widespread use of its text encoding guidelines\nin the wider academic community. This article describes the background, plans, and aims of the TEI by Example project, and why we believe it is a necessary addition to the materials currently provided by the TEI itself. The teaching\nmaterials currently available are not suited to the needs of self directed learners, and the development of stand alone, online\ntutorials in the TEI are an essential addition to the extant resources, in order to encourage and facilitate the uptake of\nTEI by both individuals and institutions.",
		"container-title": "Literary and Linguistic Computing",
		"DOI": "10.1093/llc/fqp018",
		"journalAbbreviation": "Literary and Linguistic Computing",
		"page": "297-306",
		"source": "ResearchGate",
		"title": "Teaching TEI: The need for TEI by example",
		"title-short": "Teaching TEI",
		"volume": "24",
		"author": [
			{
				"family": "Terras",
				"given": "Melissa"
			},
			{
				"family": "Branden",
				"given": "Ron"
			},
			{
				"family": "Vanhoutte",
				"given": "Edward"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2009",
					8,
					21
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/GHJX78HS",
		"type": "paper-conference",
		"abstract": "Um eine bessere Erreichbarkeit und Zugänglichkeit zu bestehenden sowie neuen Angeboten von Lehr- und Schulungsmaterialien im Bereich der Digital Humanities zu ermöglichen, sollten diese in einem zentralen Verzeichnis zur Verfügung gestellt werden. Im Rahmen des CLARIAH-DE Projekts wurde – zunächst für die Umsetzung eines Projektmeilensteins – eine Lösung gesucht, die eine übergreifende Suche in frei zugänglichen und nachnutzbaren Lehr- und Schulungsmaterialien zu Forschungsmethoden, Verfahren sowie Werkzeugen im Bereich der Digital Humanities in unterschiedlichen Plattformen und Repositorien bietet.",
		"DOI": "10.5281/zenodo.6304590",
		"event-title": "DHd2022: Kulturen des digitalen Gedächtnisses. Konferenzabstracts. Universität Potsdam & Fachhochschule Potsdam, 07. bis 11. März 2022",
		"language": "deu",
		"license": "https://creativecommons.org/licenses/by/4.0/",
		"page": "60-64",
		"publisher": "Zenodo",
		"source": "ids-pub.bsz-bw.de",
		"title": "Der CLARIAH-DE Tutorial Finder. Eine Suchumgebung für Lehr- und Schulungsmaterialien in den Digital Humanities",
		"URL": "https://ids-pub.bsz-bw.de/frontdoor/index/index/docId/11308",
		"author": [
			{
				"family": "Werthmann",
				"given": "Antonina"
			},
			{
				"family": "Gradl",
				"given": "Tobias"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					6
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/8PZYZR9P",
		"type": "article-journal",
		"container-title": "Insights",
		"issue": "1",
		"note": "ISBN: 2048-7754\npublisher: UKSG in association with Ubiquity Press",
		"title": "Diversity and inclusion in digital scholarship and pedagogy: the case of The Programming Historian",
		"volume": "32",
		"author": [
			{
				"family": "Sichani",
				"given": "Anna-Maria"
			},
			{
				"family": "Baker",
				"given": "James"
			},
			{
				"family": "Afanador Llach",
				"given": "Maria José"
			},
			{
				"family": "Walsh",
				"given": "Brandon"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/IBN67X8A",
		"type": "article-journal",
		"abstract": "Estudiar cómo se enseña y se aprende programación se ha vuelto cada vez más relevante en espacios académicos como la Facultad de Arte y Humanidades de la Universidad de los Andes, que ofrece cursos de humanidades digitales, narrativas digitales y artes electrónicas, sobretodo a la luz de debates sobre si las prácticas de los humanistas digitales pueden ser no sólo la configuración de teorías y reflexiones sino también el desarrollo de tecnologías con principios humanísticos. Este estudio utiliza un modelo de investigación crítico y participativo para analizar cómo se usan y se desarrollan las habilidades de Pensamiento Computacional (CT) en los estudiantes de estos programas y proponer un curso de Introducción al Pensamiento Computacional diseñado explícitamente para este contexto. El análisis de datos incluye entrevistas a profesores de la facultad sobre conocimiento, desarrollo y uso del PC, y artefactos como pruebas de PC y reflexiones dentro de un curso virtual de Introducción al Pensamiento Computacional. El curso incluyó conceptos de PC y una transición desde actividades como la codificación, decodificación y creación de poemas con algoritmos a la marcación de texto con HTML para finalmente llegar a programación introductoria utilizando Processing en P5.js. Entre los profesores de la facultad destacó la creencia de que el PC se desarrolla mediante el uso de softwares de edición y gestión de datos. Los resultados del curso muestran que inicialmente, los estudiantes tenían un bajo desempeño en PC, pero a lo largo del curso, el rendimiento de los estudiantes en las pruebas mejoró significativamente. Esta investigación indica que el desarrollo de la PC en la facultad de Artes y Humanidades puede robustecerse a través de un curso introductorio como el propuesto",
		"container-title": "instname:Universidad de los Andes",
		"language": "spa",
		"license": "Al consultar y hacer uso de este recurso, está aceptando las condiciones de uso establecidas por los autores.",
		"note": "Accepted: 2021-02-18T12:23:18Z\npublisher: Universidad de los Andes",
		"source": "repositorio.uniandes.edu.co",
		"title": "Desarrollar pensamiento computacional en estudiantes de artes y humanidades",
		"URL": "https://repositorio.uniandes.edu.co/handle/1992/48515",
		"author": [
			{
				"family": "Ojeda Ramírez",
				"given": "Santiago"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					6
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/V34JQH6T",
		"type": "post-weblog",
		"container-title": "Alan Liu",
		"language": "English",
		"title": "Drafts for Against the Cultural Singularity (book in progress)",
		"URL": "https://dev-liu-english-ucsb-edu-v01.pantheonsite.io/drafts-for-against-the-cultural-singularity/",
		"author": [
			{
				"family": "Liu",
				"given": "Alan"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2016",
					5,
					2
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/AF45C73P",
		"type": "article-journal",
		"abstract": "The central role that technology centers play in strengthening the digital humanities (DH) is highlighted. For library and information sciences, and particularly for academic and research libraries, working with DH is a strategic opportunity to enhance their cyberinfrastructure. It is argued that the development of DH in Spain will require providing technology centers specific to the humanities and social sciences.\nSe destaca el papel central que representan los centros tecnológicos en la consolidación de las humanidades digitales (DH). Para el área de información y documentación, y en especial para las bibliotecas académicas y de investigación, colaborar con las DH supone una oportunidad estratégica de reforzar su ciberinfraestructura. Se defiende que para la consolidación de las DH en España es necesaria la dotación de centros tecnológicos específicos para las humanidades y ciencias sociales.",
		"container-title": "El profesional de la información",
		"ISSN": "1699-2407",
		"issue": "5",
		"language": "spa",
		"note": "publisher: EPI SCP\nsection: El profesional de la información",
		"page": "453-462",
		"source": "dialnet.unirioja.es",
		"title": "Ciberinfraestructura para las humanidades digitales: una oportunidad de desarrollo tecnológico para la biblioteca académica",
		"title-short": "Ciberinfraestructura para las humanidades digitales",
		"URL": "https://dialnet.unirioja.es/servlet/articulo?codigo=4824598",
		"volume": "23",
		"author": [
			{
				"family": "Rodríguez Yunta",
				"given": "Luis"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2014"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/CNKQCUSA",
		"type": "post-weblog",
		"abstract": "Adapted version of paper last presented in full at University of Connecticut, Storrs, February 23 2017.\n\n\"Let me set the foundation first. My topic today is \"infrastructure.\" More accurately, since there is no infrastructure except as objectified perspectivally, my topic is infrastructure from the viewpoint of the digital humanities (and new media studies).\"",
		"container-title": "Critical Infrastructure Studies (CIstudies.org)",
		"language": "English",
		"title": "Toward Critical Infrastructure Studies",
		"title-short": "\"Toward Critical infrastructure Studies",
		"URL": "http://cistudies.org/wp-content/uploads/Toward-Critical-Infrastructure-Studies.pdf",
		"author": [
			{
				"family": "Liu",
				"given": "Alan"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2018"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/4ZMH3SGZ",
		"type": "book",
		"call-number": "Q175.32.K45 K57 1999",
		"event-place": "Cambridge, Mass",
		"ISBN": "978-0-674-25893-8",
		"number-of-pages": "329",
		"publisher": "Harvard University Press",
		"publisher-place": "Cambridge, Mass",
		"source": "Library of Congress ISBN",
		"title": "Epistemic cultures: how the sciences make knowledge",
		"title-short": "Epistemic cultures",
		"author": [
			{
				"family": "Knorr Cetina",
				"given": "Karin"
			}
		],
		"issued": {
			"date-parts": [
				[
					"1999"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/7PBKBZFL",
		"type": "article-journal",
		"abstract": "Many individuals claim that Piaget's theory of cognitive development is empirically false or substantially disconfirmed by empirical research. Although there is substance to such a claim, any such conclusion must address three increasingly problematic issues about the possibility of providing an empirical test of Piaget's genetic epistemology: (1) the empirical underdetermination of theory by empirical evidence, (2) the empirical difficulty of testing competence-type explanations, and (3) the difficulty of empirically testing epistemic norms. This is especially true of a central epistemic construct in Piaget's theory — the epistemic subject. To illustrate how similar problems of empirical testability arise in the physical sciences, I briefly examine the case of Galileo and the correlative difficulty of empirically testing Galileo's laws. I then point out some important epistemological similarities between Galileo and Piaget together with correlative changes needed in science studies methodology. I conclude that many psychologists and science educators have failed to appreciate the difficulty of falsifying Piaget's theory because they have tacitly adopted a philosophy of science at odds with the paradigm-case of Galileo.",
		"container-title": "Science & Education",
		"DOI": "10.1007/BF00592203",
		"ISSN": "1573-1901",
		"issue": "2",
		"journalAbbreviation": "Sci Educ",
		"language": "en",
		"page": "137-148",
		"source": "Springer Link",
		"title": "Piaget's epistemic subject and science education: Epistemological vs. psychological issues",
		"title-short": "Piaget's epistemic subject and science education",
		"URL": "https://doi.org/10.1007/BF00592203",
		"volume": "2",
		"author": [
			{
				"family": "Kitchener",
				"given": "Richard F."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"1993",
					6,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5EM52NU8",
		"type": "book",
		"call-number": "AZ105 .S88 2016",
		"collection-title": "Digital humanities",
		"event-place": "Ann Arbor",
		"ISBN": "978-0-472-05306-3",
		"number-of-pages": "279",
		"publisher": "University of Michigan Press",
		"publisher-place": "Ann Arbor",
		"source": "Library of Congress ISBN",
		"title": "Big Digital Humanities: imagining a meeting place for the humanities and the digital",
		"title-short": "Big Digital Humanities",
		"author": [
			{
				"family": "Svensson",
				"given": "Patrik"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2016"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/CP87A26M",
		"type": "article-journal",
		"abstract": "How do the power dynamics of actors in digital knowledge production define the contours of global science and humanities? Where are scholars now in their efforts to improve a networked, global academic system based on the values of equal access to resources, inclusive participation, and the diversity of epistemologies? This article intervenes in these questions by discussing social dimensions of global knowledge infrastructure—connection, standardization, and access—to understand the specification and materialization of global digital humanities (DH). As digital practices expand across the world, the DH community struggles to ensure inclusive participation and equal opportunities in developing the field. This article shows that discrepancies in global DH lie at the root of existing infrastructure inequalities. Drawing on science and technology studies, it then argues that in order to overcome these imbalances, the academic community can seek the ‘infrastructuring’ of DH. Infrastructuring is an analytical concept that shifts attention from ‘structure’ to ‘process’ of co-creation in the vein of participatory design that foregrounds public engagement, shared interest, and long-term relationships with stakeholders to create networks from which equal opportunities and new forms of connections can emerge. This would involve building an inclusive network of unique nodes of local communities on top of the global knowledge infrastructure.",
		"container-title": "Digital Scholarship in the Humanities",
		"DOI": "10.1093/llc/fqab086",
		"ISSN": "2055-7671",
		"issue": "2",
		"journalAbbreviation": "Digital Scholarship in the Humanities",
		"page": "534-550",
		"source": "Silverchair",
		"title": "Infrastructuring digital humanities: On relational infrastructure and global reconfiguration of the field",
		"title-short": "Infrastructuring digital humanities",
		"URL": "https://doi.org/10.1093/llc/fqab086",
		"volume": "37",
		"author": [
			{
				"family": "Pawlicka-Deger",
				"given": "Urszula"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022",
					6,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WVWZ2F24",
		"type": "document",
		"title": "Pawlicka-Deger_2022_Infrastructuring digital humanities.pdf"
	},
	{
		"id": "http://zotero.org/users/163570/items/CC76UMIT",
		"type": "article-journal",
		"abstract": "This article advances the thesis that three decades of investments by national and international funders, combined with those of scholars, technologists, librarians, archivists, and their institutions, have resulted in a digital infrastructure in the humanities that is now capable of supporting end-to-end research workflows. The article refers to key developments in the epigraphy and paleography of the premodern period. It draws primarily on work in classical studies but also highlights related work in the adjacent disciplines of Egyptology, ancient Near East studies, and medieval studies. The argument makes a case that much has been achieved but it does not declare “mission accomplished.” The capabilities of the infrastructure remain unevenly distributed within and across disciplines, institutions, and regions. Moreover, the components, including the links between steps in the workflow, are generally far from user-friendly and seamless in operation. Because further refinements and additional capacities are still much needed, the article concludes with a discussion of key priorities for future work.",
		"container-title": "International Journal on Digital Libraries",
		"DOI": "10.1007/s00799-022-00332-3",
		"ISSN": "1432-1300",
		"journalAbbreviation": "Int J Digit Libr",
		"language": "en",
		"source": "Springer Link",
		"title": "The emerging digital infrastructure for research in the humanities",
		"URL": "https://doi.org/10.1007/s00799-022-00332-3",
		"author": [
			{
				"family": "Waters",
				"given": "Donald J."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2022",
					10,
					7
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/EB24T8SP",
		"type": "article-journal",
		"container-title": "Digital Humanities Quarterly",
		"ISSN": "1938-4122",
		"issue": "3",
		"journalAbbreviation": "DHQ",
		"title": "Infrastructure and Social Interaction: Situated Research Practices in Digital Humanities in India",
		"title-short": "Infrastructure and Social Interaction",
		"volume": "014",
		"author": [
			{
				"family": "T",
				"given": "Shanmugapriya"
			},
			{
				"family": "Menon",
				"given": "Nirmala"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020",
					9,
					25
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5524UAZW",
		"type": "article-journal",
		"container-title": "Digital Humanities Quarterly",
		"ISSN": "1938-4122",
		"issue": "3",
		"journalAbbreviation": "DHQ",
		"title": "Digital Humanities as Epistemic Cultures: How DH Labs Make Knowledge, Objects, and Subjects",
		"title-short": "Digital Humanities as Epistemic Cultures",
		"volume": "014",
		"author": [
			{
				"family": "Malazita",
				"given": "James"
			},
			{
				"family": "Teboul",
				"given": "Ezra J."
			},
			{
				"family": "Rafeh",
				"given": "Hined"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2020",
					9,
					25
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WCZPNA2K",
		"type": "document",
		"title": "Snapshot",
		"URL": "https://academic.oup.com/dsh/article/37/2/534/6372159?login=false",
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QQIBBVPK",
		"type": "webpage",
		"abstract": "We describe how attention to the everyday life of infrastructural assemblages promises new ways to think about time, publics, and biopolitics",
		"container-title": "Society for Cultural Anthropology",
		"language": "en",
		"title": "Introduction: The Infrastructure Toolbox",
		"title-short": "Introduction",
		"URL": "https://culanth.org/fieldsights/introduction-the-infrastructure-toolbox",
		"author": [
			{
				"family": "Appel",
				"given": "Hannah"
			},
			{
				"family": "Anand",
				"given": "Nikhil"
			},
			{
				"family": "Gupta",
				"given": "Akhil"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015",
					9,
					24
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/FJ4IDER9",
		"type": "post-weblog",
		"language": "en-US",
		"title": "About – Tactical Humanities Lab",
		"URL": "https://tactical.wp.rpi.edu/about/",
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/QISTL8EZ",
		"type": "article-journal",
		"abstract": "This essay addresses emerging open scholarly practices in transnational contexts, in particular in the Eastern Arab countries. It also describes some of the larger contours of the globalization in higher education in the regions of Middle East/North Africa (MENA) and Asia. Drawing upon work in the field in Lebanon and the Gulf States, it discusses some of the opportunities and challenges for open scholarship in the region, notably a gap in knowledge infrastructure. Finally, it argues that an important opportunity has emerged for the region’s globally connected institutions of higher education to shape and enact new knowledge environments.",
		"container-title": "Pop! Public. Open. Participatory",
		"issue": "1",
		"language": "en",
		"note": "publisher: CISP Press",
		"source": "popjournal.ca",
		"title": "Enacting Open Scholarship in Transnational Contexts",
		"URL": "https://popjournal.ca/issue01/wrisley",
		"author": [
			{
				"family": "Wrisley",
				"given": "David Joseph"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					20
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2019",
					10,
					31
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5FTMZ8UQ",
		"type": "article-journal",
		"container-title": "Digital Humanities Quarterly",
		"ISSN": "1938-4122",
		"issue": "2",
		"journalAbbreviation": "DHQ",
		"title": "Relocating Complexity: The Programming Historian and Multilingual Static Site Generation",
		"title-short": "Relocating Complexity",
		"volume": "016",
		"author": [
			{
				"family": "Lincoln",
				"given": "Matthew"
			},
			{
				"family": "Isasi",
				"given": "Jennifer"
			},
			{
				"family": "Melton",
				"given": "Sarah"
			},
			{
				"family": "Laramée",
				"given": "François Dominic"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022",
					6,
					25
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/5P924PIP",
		"type": "post-weblog",
		"abstract": "GitHub Pages allow you to publish web content to a github.com subdomain named after your username. With Pages, publishing web content becomes as easy as pushing to your GitHub repository. If you create a repository named you.github.com, where you is your username, and push content to it, we’ll automatically publish that to http://you.github.com. No FTP, […]",
		"container-title": "The GitHub Blog",
		"language": "en-US",
		"title": "GitHub Pages",
		"URL": "https://github.blog/2008-12-18-github-pages/",
		"author": [
			{
				"family": "Preston-Werner",
				"given": "Tom"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2008",
					12,
					18
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/R5BTEYCP",
		"type": "post-weblog",
		"container-title": "The Programming Historian",
		"title": "How We Moved the Programming Historian to GitHub Pages",
		"URL": "https://programminghistorian.org/posts/how-we-moved-to-github",
		"author": [
			{
				"family": "McDaniel",
				"given": "Caleb"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2014",
					11,
					5
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WCJ2T8DA",
		"type": "post-weblog",
		"container-title": "Tom Preston-Werner",
		"language": "en",
		"title": "Blogging Like a Hacker",
		"URL": "https://tom.preston-werner.com/2008/11/17/blogging-like-a-hacker.html",
		"author": [
			{
				"family": "Preston-Werner",
				"given": "Tom"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2008",
					11,
					17
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/IRX92Y8A",
		"type": "article-magazine",
		"container-title": "DH Commons",
		"issue": "1",
		"language": "en",
		"title": "Editorial Sustainability and Open Peer Review at Programming Historian",
		"URL": "https://web.archive.org/web/20180713014622/http://dhcommons.org/journal/issue-1/editorial-sustainability-and-open-peer-review-programming-historian",
		"author": [
			{
				"family": "Gibbs",
				"given": "Fred"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/WZQQIKFY",
		"type": "article-journal",
		"container-title": "Digital Humanities Quarterly",
		"ISSN": "1938-4122",
		"issue": "2",
		"journalAbbreviation": "DHQ",
		"title": "Minimizing Computing Maximizes Labor",
		"volume": "016",
		"author": [
			{
				"family": "Dombrowski",
				"given": "Quinn"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022",
					6,
					25
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/99S6FXLJ",
		"type": "post-weblog",
		"container-title": "The Programming Historian",
		"title": "Infrastructure for Collaboration: Catching Dead Links And Errors",
		"URL": "https://programminghistorian.org/posts/infrastructure-at-ph",
		"author": [
			{
				"family": "Lincoln",
				"given": "Matthew"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					1,
					22
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2017",
					7,
					31
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/H2BR4VR4",
		"type": "chapter",
		"abstract": "An awareness that communication is always a mediated experience, combined with the skills of forensic analysis and bibliographic imagination, is as relevant to books as to any other material form, including electronic records. At the heart of the critical enterprise is an understanding of digital materiality, not framed as the intangibility of cyberspace using the superficial distinction between physical, surrogate, and virtual, but as the palpable bits and bytes of electronic hardware and software that are ubiquitous, that leave traces, and that can be read as evidence of the creation, dissemination, reception, and preservation of these new communication forms. Scholars like Matt Kirschenbaum and Alan Galey have rendered digital forensics necessary for the digital humanist's intellectual toolkit. This chapter surveys and extends those understandings by exploring how digital materiality is captured in metadata, in interfaces, in time- and date-stamped information processing, in the multivariate interactions of users and forms. In effect, digital documents reveal their own stories if you know where to look, what to analyze, and how to read their material legacy.",
		"container-title": "A New Companion to Digital Humanities",
		"ISBN": "978-1-118-68060-5",
		"language": "en",
		"note": "section: 22\n_eprint: https://onlinelibrary.wiley.com/doi/pdf/10.1002/9781118680605.ch22\nDOI: 10.1002/9781118680605.ch22",
		"page": "322-330",
		"publisher": "John Wiley & Sons, Ltd",
		"source": "Wiley Online Library",
		"title": "Digital Materiality",
		"URL": "https://onlinelibrary.wiley.com/doi/abs/10.1002/9781118680605.ch22",
		"author": [
			{
				"family": "Shep",
				"given": "Sydney J."
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					3,
					6
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2015"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/RWKAWUEW",
		"type": "book",
		"ISBN": "978-90-04-40035-1",
		"note": "DOI: 10.1163/9789004400351",
		"publisher": "BRILL",
		"source": "DOI.org (Crossref)",
		"title": "Among Digitized Manuscripts. Philology, Codicology, Paleography in a Digital World",
		"URL": "https://brill.com/view/title/56196",
		"author": [
			{
				"family": "Lit",
				"given": "L.W.C.",
				"non-dropping-particle": "van"
			}
		],
		"accessed": {
			"date-parts": [
				[
					"2023",
					3,
					6
				]
			]
		},
		"issued": {
			"date-parts": [
				[
					"2020",
					1,
					1
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/8TKXX7SX",
		"type": "chapter",
		"call-number": "AZ105 .S43 2019",
		"collection-title": "Digital research in the arts and humanities",
		"container-title": "The shape of data in the digital humanities: modeling texts and text-based resources",
		"event-place": "London ; New York",
		"ISBN": "978-1-4724-4324-3",
		"page": "99-116",
		"publisher": "Routledge, Taylor & Francis Group",
		"publisher-place": "London ; New York",
		"source": "Library of Congress ISBN",
		"title": "How modeling standards evolve. The case of TEI",
		"editor": [
			{
				"family": "Flanders",
				"given": "Julia"
			},
			{
				"family": "Jannidis",
				"given": "Fotis"
			}
		],
		"author": [
			{
				"family": "Burnard",
				"given": "Lou"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2019"
				]
			]
		}
	},
	{
		"id": "http://zotero.org/users/163570/items/CP5F9QRY",
		"type": "chapter",
		"call-number": "AZ105",
		"collection-title": "Debates in the digital humanities",
		"container-title": "Global debates in the digital humanities",
		"event-place": "Minneapolis",
		"ISBN": "978-1-4529-6710-3",
		"page": "225-238",
		"publisher": "University of Minnesota Press",
		"publisher-place": "Minneapolis",
		"source": "Library of Congress ISBN",
		"title": "Developing new literacy skills and digital scholarship infrastructures in the Global South",
		"editor": [
			{
				"family": "Fiormonte",
				"given": "Domenico"
			},
			{
				"family": "Chaudhuri",
				"given": "Sukanta"
			},
			{
				"family": "Ricaurte",
				"given": "Paola"
			}
		],
		"author": [
			{
				"family": "Afanador Llach",
				"given": "Maria José"
			},
			{
				"family": "Lombana",
				"given": "Andrés"
			}
		],
		"issued": {
			"date-parts": [
				[
					"2022"
				]
			]
		}
	}
]