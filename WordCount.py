import itertools
import ntpath
import csv
import re


class WordCount(object):
    def __init__(self):  # , filepath, label=""):
        self.opportunity = ['advancement', 'advantage', 'befalling', 'break', 'chance', 'connection', 'contingency',
                   'convenience',
                   'cut', 'expect', 'expectation', 'expects', 'expediency', 'fair shake', 'favorability', 'favorable',
                   'fighting chance', 'fitness', 'fling', 'fortuity', 'fortune', 'hope', 'luck', 'momentous',
                   'momentum',
                   'momentus', 'occasion', 'opening', 'opportune', 'opportunisitic', 'opportunistic', 'opportunities',
                   'opportunity', 'optimism', 'optimist', 'optimistic', 'outlook', 'possibility', 'prospect',
                   'prospects',
                   'prosperity', 'prosperous', 'recourse', 'stimulating', 'successful', 'suitable', 'time', 'turn',
                   'upbeat', 'viable']
        self.threat = ['alarming', 'alarming fateful', 'apocalyptic', 'assault', 'baleful', 'baneful', 'black', 'cautionary',
              'challenging', 'comminatory', 'conflict', 'constrained', 'crisis', 'crunch', 'danger', 'dangerous',
              'demur',
              'dire', 'fateful', 'foreboding', 'grim', 'hazard', 'ill-boding', 'imminent', 'impendent', 'impending',
              'inauspicious', 'intimidating', 'jeopardy', 'looming', 'loss', 'loury', 'lowering', 'lowery', 'menace',
              'minacious', 'minatory', 'negative', 'omen', 'peril', 'portending', 'portent', 'risk', 'sinister',
              'stressful', 'sword of damocles', 'trial dire', 'ugly', 'unlucky', 'unpropitious', 'unsafe', 'urgent',
              'warning']
        self.enactment = ['absorb', 'access', 'accomplish', 'accrue', 'achieve', 'acquire', 'acquisition', 'act', 'action',
                 'active',
                 'activity', 'actualize', 'advance', 'affect', 'affiliate', 'aggrandizement', 'agitate', 'alacrity',
                 'alertness', 'ally', 'alter', 'amalgamat', 'amalgamate', 'amass', 'amplif', 'annex', 'appeal',
                 'assimilate', 'attack', 'attain', 'attribute', 'augment', 'bankrupt', 'barnstorm', 'battle', 'blend',
                 'boost', 'campaign', 'cement', 'censure', 'centralize', 'change', 'charge', 'cite', 'coalesce',
                 'combat',
                 'combine', 'commission', 'complain', 'complete', 'compound', 'conflict', 'conglomerate', 'consolidate',
                 'consummate', 'contend', 'contest', 'converge', 'crusade', 'cultivate', 'deconstruct', 'denounce',
                 'develop', 'developing', 'develops', 'dilation', 'disassemble', 'disinherit', 'dismantle', 'dispute',
                 'distention', 'divest', 'divestiture', 'effect', 'enact', 'encounter', 'engage', 'engagement',
                 'enlarge',
                 'enterprise', 'environment', 'environs', 'execute', 'exercise', 'exert', 'expand', 'expands',
                 'expansion',
                 'exploit', 'extension', 'fight', 'finish', 'force', 'forfeit', 'fulfill', 'further', 'fuse',
                 'gradual increase', 'gradually increase', 'grow', 'grows', 'growth', 'impeach', 'implicate', 'impute',
                 'incorporate', 'incriminate', 'inculpate', 'indict', 'induce', 'industry', 'influence', 'intermingle',
                 'intervene', 'intervention', 'investment banker', 'join', 'league', 'lobby', 'manage', 'maneuver',
                 'manipulate', 'market', 'marry', 'meld', 'merge', 'mingle', 'modify', 'move', 'network', 'niche',
                 'nook',
                 'occupy', 'operate', 'operation', 'oust', 'perform', 'persuade', 'pitch', 'planted', 'plug',
                 'politick',
                 'pool', 'press', 'pressure', 'proceed', 'proceeds', 'process', 'procure', 'progress', 'progression',
                 'promote', 'prosecute', 'province', 'purchase', 'purview', 'react', 'realize', 'region', 'relinquish',
                 'remove', 'request', 'resist', 'resolve', 'respond', 'rival', 'rush', 'sacrifice', 'scope', 'sector',
                 'secure', 'sell', 'separate', 'solicit', 'stir', 'strive', 'struggle', 'sway', 'syndicate',
                 'synthesize',
                 'team', 'team up', 'terrain', 'territory', 'thrust', 'transact', 'turgescence', 'undertake', 'unite',
                 'urge', 'vie', 'win']
        self.org_iden = ['abreast', 'accede', 'acceded', 'accedes', 'acceding', 'accept', 'accepted', 'accepting', 'accepts',
                'accommodate', 'accommodated', 'accommodates', 'accommodation', 'accompanied', 'accompanies',
                'accompany',
                'accompanying', 'accord', 'accords', 'adhere', 'adhered', 'adheres', 'adhering', 'admit', 'admits',
                'admitted', 'admitting', 'affiliate', 'affiliated', 'affiliates', 'affiliating', 'affiliation',
                'affiliations', 'affinities', 'affinity', 'affirm', 'affirmed', 'affirming', 'affirms', 'aggregate',
                'aggregated', 'aggregates', 'aggregating', 'agree', 'agreeable', 'agreed', 'agreeing', 'agrees', 'akin',
                'align', 'aligned', 'aligning', 'alignment', 'alignments', 'aligns', 'alike', 'all', 'alliances',
                'allied',
                'allies', 'allow', 'allowed', 'allowing', 'allows', 'ally', 'alongside', 'altogether', 'amalgamate',
                'amalgamated', 'amalgamating', 'amalgamation', 'amalgamations', 'ambience', 'analogies', 'analogous',
                'analogy', 'ancestry', 'annex', 'annexed', 'annexes', 'annexing', 'approve', 'approved', 'approves',
                'approving', 'arbitrate', 'arbitrated', 'arbitrating', 'arbitration', 'arbitrations', 'arrange',
                'arranged',
                'arrangement', 'arrangements', 'arranges', 'arranging', 'assemblage', 'assemblages', 'assemble',
                'assembled', 'assemblies', 'assembling', 'assembly', 'assent', 'assented', 'assenting', 'assents',
                'associate', 'associated', 'associates', 'associating', 'association', 'associations', 'atmosphere',
                'aura',
                'authentic', 'balance', 'balance-of-power', 'balanced', 'balances', 'balancing', 'bandwagon',
                'bandwagons',
                'basic', 'bedfellow', 'bedfellows', 'bi-lateral', 'bilingual', 'bind', 'binding', 'binds', 'bipartisan',
                'birthright', 'blend', 'blended', 'blending', 'blends', 'bloc', 'blocs', 'bond', 'bonded', 'bonding',
                'bonds', 'bound', 'brotherhood', 'brotherhoods', 'buddies', 'buddy', 'cahoots', 'camaraderie',
                'cardinal',
                'caretaker', 'caretakers', 'caretaking', 'categorical', 'caucus', 'caucused', 'caucuses', 'caucusing',
                'ceaseless', 'center', 'character', 'chief', 'chum', 'chums', 'circumstances', 'clan', 'clans', 'class',
                'class-action', 'class-based', 'classes', 'classification', 'classifications', 'classified',
                'classifies',
                'classify', 'classifying', 'classmate', 'classmates', 'climate', 'clique', 'cliques', 'close',
                'closeness',
                'closer', 'closest', 'club', 'clubs', 'cluster', 'clustered', 'clustering', 'clusters', 'co-worker',
                'coalition', 'coalitions', 'cohere', 'coherent', 'cohesive', 'cohort', 'cohorts', 'coincide',
                'coincided',
                'coincides', 'coinciding', 'collaborate', 'collaborated', 'collaborates', 'collaboration',
                'collaborations',
                'colleague', 'colleagues', 'collection', 'collections', 'collective', 'collectives', 'collude',
                'colluded',
                'colludes', 'colluding', 'collusion', 'collusions', 'combination', 'combinations', 'combine',
                'combined',
                'combines', 'combining', 'commend', 'commended', 'commending', 'commends', 'commission', 'commissions',
                'committee', 'committees', 'communal', 'commune', 'communes', 'communities', 'companion',
                'companionable',
                'companions', 'companionship', 'comparable', 'comparably', 'compatibilities', 'compatibility',
                'compatible',
                'complement', 'complemented', 'complementing', 'complements', 'complied', 'complies', 'compliment',
                'compliments', 'comply', 'complying', 'composite', 'composites', 'compromise', 'compromised',
                'compromises',
                'compromising', 'comrade', 'comrades', 'concede', 'conceded', 'concedes', 'conceding', 'concert',
                'concerted', 'concession', 'concessions', 'concur', 'concurred', 'concurrent', 'concurring', 'concurs',
                'confirm', 'confirmation', 'confirmations', 'confirmed', 'confirming', 'confirms', 'conform',
                'conformed',
                'conforming', 'conforms', 'congenial', 'congregate', 'congregates', 'congregating', 'congregations',
                'conjoin', 'conjoined', 'conjoining', 'conjoins', 'conjunction', 'conjunctions', 'connect', 'connected',
                'connecting', 'connection', 'connections', 'connects', 'consensus', 'consent', 'consented',
                'consenting',
                'consents', 'consistencies', 'consistency', 'consistent', 'consolidate', 'consolidated', 'consolidates',
                'consolidating', 'consolidation', 'consolidations', 'consonance', 'conspiracies', 'conspiracy',
                'conspire',
                'conspired', 'conspires', 'constant', 'contact', 'contacted', 'contacting', 'context', 'continual',
                'continuous', 'contracted', 'contracting', 'contributed', 'contributes', 'contribution',
                'contributions',
                'convene', 'convened', 'convenes', 'convening', 'converge', 'converged', 'converges', 'converging',
                'cooperate', 'cooperated', 'cooperates', 'cooperation', 'cooperative', 'cooperatively', 'coordinate',
                'coordinated', 'coordinates', 'coordinating', 'coordination', 'copied', 'copies', 'copy', 'copying',
                'cordial', 'correlate', 'correlated', 'correlates', 'correlating', 'correlation', 'correlations',
                'corresponding', 'covenant', 'covenants', 'cronies', 'crony', 'culture', 'customary', 'customs',
                'dealings',
                'definite', 'definitive', 'dependable', 'dependence', 'dependent', 'devote', 'devoted', 'devotes',
                'devoting', 'discrete', 'disparate', 'disposition', 'distinct', 'distinctive', 'divergent', 'diverse',
                'dominant', 'donate', 'donated', 'donates', 'donation', 'donations', 'duplicate', 'duplicated',
                'duplicates', 'duplicating', 'd\xe9tente', 'echo', 'echoed', 'echoes', 'echoing', 'elemental',
                'embrace',
                'embraced', 'embraces', 'embracing', 'empathize', 'empathized', 'empathizes', 'empathizing', 'empathy',
                'endorse', 'endorsed', 'endorses', 'endorsing', 'enduring', 'environ', 'equal', 'equalities',
                'equality',
                'equally', 'equate', 'equated', 'equating', 'equidistant', 'equivalence', 'equivalent', 'essential',
                'eternal', 'everybody', 'exchange', 'exchanged', 'exchanges', 'exchanging', 'experience', 'explicit',
                'express', 'facilitate', 'facilitated', 'facilitates', 'facilitating', 'faithful', 'familiar',
                'familiarity', 'families', 'federation', 'federations', 'feeling', 'fellowship', 'fellowships', 'focal',
                'folklore', 'folkways', 'foremost', 'friendliness', 'friendship', 'friendships', 'fundamental', 'fuse',
                'fused', 'fusing', 'fusion', 'genuine', 'get-together', 'get-togethers', 'give-and-take', 'go-between',
                'habitual', 'help', 'helped', 'helping', 'helpmate', 'helpmates', 'helps', 'homogeneity', 'homogeneous',
                'hospitable', 'hospitality', 'identical', 'illustrative', 'immutable', 'important', 'incessant',
                'include',
                'included', 'includes', 'including', 'inclusion', 'incorporate', 'incorporated', 'incorporates',
                'incorporating', 'indispensable', 'indulge', 'indulged', 'indulgence', 'indulgences', 'indulges',
                'indulging', 'inherent', 'inmost', 'inner', 'integrate', 'integrated', 'integrates', 'integrating',
                'integration', 'interact', 'interacted', 'interacting', 'interaction', 'interactions', 'intercede',
                'interceded', 'intercedes', 'interceding', 'interchangeable', 'interconnect', 'interconnected',
                'interconnecting', 'interconnection', 'interconnections', 'interconnects', 'intercourse', 'interior',
                'intermesh', 'intermeshed', 'intermeshes', 'intermeshing', 'interrelate', 'interrelated',
                'interrelating',
                'interrelations', 'intersect', 'intersected', 'intersecting', 'intersection', 'intersections',
                'intertwine',
                'intertwined', 'intertwines', 'intertwining', 'intimacies', 'intimacy', 'intimate', 'intrinsic',
                'invariable', 'join', 'joined', 'joining', 'joins', 'joint', 'junction', 'junctions', 'key', 'kindred',
                'kinship', 'lasting', 'leading', 'liaison', 'liaisons', 'like-minded', 'like-mindedness', 'likeness',
                'likenesses', 'likewise', 'lineage', 'link', 'linked', 'linking', 'links', 'lucid', 'main', 'marked',
                'master', 'matched', 'matching', 'mate', 'mated', 'mates', 'mating', 'mediate', 'mediated', 'mediates',
                'mediating', 'medium', 'meetings', 'milieu', 'mingle', 'mingled', 'mingling', 'mood', 'mutual',
                'mutuality',
                'negotiable', 'negotiate', 'negotiated', 'negotiating', 'negotiation', 'negotiations', 'networked',
                'networking', 'networks', 'noticeable', 'offer', 'offered', 'offering', 'offers', 'oneness',
                'organization',
                'organizational', 'orientation', 'our', 'ourself', 'ourselves', 'palatable', 'parallel', 'parallels',
                'paramount', 'parity', 'partake', 'partakes', 'partaking', 'participate', 'participated',
                'participates',
                'participation', 'particular', 'parties', 'partner', 'partners', 'partnership', 'partnerships',
                'partook',
                'party', 'party-line', 'patent', 'patronage', 'peculiar', 'peer', 'peers', 'permanent', 'permission',
                'permit', 'permits', 'permitted', 'permitting', 'perpetual', 'persevering', 'persistent', 'pivotal',
                'pledge', 'pledged', 'pledges', 'pledging', 'predominant', 'primary', 'prime', 'principle',
                'public-interest', 'public-service', 'public-spirited', 'rapport', 'ratified', 'ratifies', 'ratify',
                'reciprocal', 'reciprocate', 'reciprocated', 'reciprocates', 'reciprocating', 'reciprocation',
                'reciprocity', 'recognizable', 'recruit', 'recruited', 'recruiting', 'recruits', 'regular', 'relate',
                'related', 'relates', 'relating', 'relations', 'relationship', 'relationships', 'rendezvous',
                'reproduce',
                'reproduced', 'reproduces', 'reproducing', 'resemblance', 'resemblances', 'resemble', 'resembled',
                'resembling', 'resolute', 'reunite', 'reunited', 'reuniting', 'salient', 'same', 'sameness', 'scene',
                'schoolmate', 'schoolmates', 'self-denial', 'self-denying', 'self-effacement', 'self-effacing',
                'self-sacrifice', 'self-sacrificing', 'selfless', 'selfsame', 'setting', 'share', 'shared', 'shares',
                'sharing', 'significant', 'similar', 'similarities', 'sisterhood', 'sisterhoods', 'situation',
                'sociability', 'sociable', 'socialization', 'socialize', 'socialized', 'socializing', 'special',
                'specific',
                'spirit', 'stable', 'staunch', 'steadfast', 'steady', 'subscribe', 'subscribed', 'subscribes',
                'subscribing', 'sufferance', 'surroundings', 'symmetrical', 'symmetry', 'sympathize', 'sympathized',
                'sympathizes', 'sympathizing', 'sympathy', 'synchronize', 'synchronized', 'synchronizes',
                'synchronizing',
                'synchronous', 'syndicate', 'syndicates', 'synonymous', 'syntheses', 'synthesis', 'synthetic',
                'tantamount',
                'teamed', 'teaming', 'teammate', 'teammates', 'teams', 'teamwork', 'temperament', 'tenor', 'terrain',
                'territory', 'their', 'them', 'they', 'tie-in', 'tie-ins', 'timbre', 'together', 'tolerance',
                'tolerant',
                'tolerate', 'tolerates', 'tolerating', 'toleration', 'tone', 'townspeople', 'turf', 'twin', 'twins',
                'unalterable', 'unambiguous', 'unanimity', 'unanimous', 'unchanging', 'underlying', 'unequivocal',
                'unfailing', 'unflagging', 'unflappable', 'unfluctuating', 'unification', 'unified', 'uniform', 'unify',
                'unifying', 'uninterrupted', 'unions', 'unique', 'unison', 'unit', 'unite', 'unites', 'uniting',
                'units',
                'unity', 'unmistakable', 'unrelenting', 'unremitting', 'unties', 'unvarying', 'unwavered', 'unwavering',
                'us', 'vital', 'vouch', 'vouched', 'vouches', 'vouching', 'warrant', 'warranted', 'warranting',
                'warrants',
                'we', 'well-beloved', 'well-disposed', 'well-inclined', 'well-loved', 'well-wisher', 'well-wishers',
                'whole', 'wholly', 'willing', 'willingly']
        self.lists_to_use = []
        self.list_names = []
        self.corpora = []
        self.corpora_names = []
        self.counts = []
        self.counters = []

    def add_corpus(self, filepath, label=""):
        if label == "":
            self.corpora_names.append(ntpath.basename(filepath))
        else:
            self.corpora_names.append(ntpath.basename(label))
        self.corpora.append(self.utf8_to_ascii(read_txt(filepath)).decode('unicode_escape').encode('ascii', 'ignore'))

    def scrub_list(self, lst):
        lst = list(map(lambda x: x.lower(), lst))
        return list(sorted(set(lst)))

    def utf8_to_ascii(self, text):
        text = text.replace(u'\u2014', '-')
        text = text.replace(u'\u2013', '-')
        exclude = set('!"#$%&()*+,./:;<=>?@[\]^_`{|}~')
        exclude.add(u'\u2018')  # '
        exclude.add(u'\u2019')  # '
        exclude.add(u'\u201c')  # "
        exclude.add(u'\u201d')  # "
        exclude.add(u'\u2022')  # bullet point
        exclude.add(u'\u2026')  # ...

        for c in exclude:
            text = text.replace(c, ' ')

        return text

    def upload_list(self, csv_file, lst_name):
        # Uploading all Organizational Identity words into a list called new_list
        new_list = []
        iter_count = 0
        with open(csv_file, 'rb') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                new_list.append(row)
                iter_count += 1
            new_list = list(itertools.chain(*new_list))
            new_list = self.scrub_list(new_list)
            self.add_list(new_list, lst_name)

    def add_list(self, lst, lst_name):
        # need to check is list exists
        self.lists_to_use.append(lst)
        self.list_names.append(lst_name)

    def count_words(self):
        for corpus in self.corpora:
            counts = []
            for lst in self.lists_to_use:
                count = 0
                for word in lst:
                    count += len(re.findall(" " + word + " ", corpus))
                counts.append(count)
            self.counters.append(counts)

    def to_html(self):
        result = "<table border=1><tr>"
        result += "<td align='center'>file</td>"
        for name in self.list_names:
            result += "<td align='center'>" + name + "</td>"
        result += "</tr><tr>"
        for i in range(len(self.corpora_names)):
            result += "</tr><tr><td align='center'>" + self.corpora_names[i] + "</td>"
            for counts in self.counters[i]:
                result += "<td align='center'>" + str(counts) + "</td>"
        result += "</tr></table?"
        return result

    def display(self):
        print '{:>8}'.format("file"),
        for name in self.list_names:
            print '{:>8}'.format(name),
        for i in range(len(self.corpora)):
            print '\n{:>8}'.format(self.corpora_names[i]),
            for counts in self.counters[i]:
                print '{:>8}'.format(counts),

    def save_to_csv(self):
        with open('results.csv', 'wb') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow(["file"] + self.list_names)
        csvfile.close()
        with open('results.csv', 'a') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in range(len(self.corpora)):
                spamwriter.writerow([self.corpora_names[i]] + self.counters[i])

    def save_list(self, list_name):
        index = -1
        count = 0
        for lst in self.list_names:
            if lst == list_name:
                index = count
            count += 1
        if index == -1:
            print "\nList", list_name, "not found"
        else:
            with open("Dictionaries/" + self.list_names, 'w') as file:
                file.write(", ".join(self.lists_to_use[index]))
            file.close()


def read_txt(filepath):
    try:
        with open(filepath, 'r') as myfile:
            return myfile.read().decode("utf-8").lower()
    except IOError:
        print "could not read", filepath


def hardiness():
    hardi = WordCount()
    hardi.add_corpus("TestSuite/JPMorgan2000_3paragraphs.txt", label="JPMsort")
    hardi.add_corpus("TestSuite/JP Morgan/JP Morgan2000docx.txt", label="JPM")
    hardi.add_list(hardi.threat, "threat")
    hardi.add_list(hardi.enactment, "enactment")
    hardi.add_list(hardi.opportunity, "opportunity")
    hardi.add_list(hardi.org_iden, "org_id")
    hardi.count_words()
    hardi.display()
    hardi.save_to_csv()
    return hardi.to_html()


def main():
    hardiness()
    #hardiness("TestSuite/JP Morgan/JP Morgan2000docx.txt", label="JPM")


if __name__ == "__main__":
    main()
