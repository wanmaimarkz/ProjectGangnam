"""Project"""
import folium
from folium import plugins

def dist_between_two_lat_lon(*args):
    """calculate distance"""
    from math import asin, cos, radians, sin, sqrt
    lat1, lat2, long1, long2 = map(radians, args)

    dist_lats = abs(lat2 - lat1) 
    dist_longs = abs(long2 - long1) 
    a = sin(dist_lats/2)**2 + cos(lat1) * cos(lat2) * sin(dist_longs/2)**2
    c = asin(sqrt(a)) * 2
    radius_earth = 6378
    return c * radius_earth

def find_closest_lat_lon(data, v):
    """Calculate the distance of the nearest place"""
    try:
        return min(data, key=lambda p: dist_between_two_lat_lon(v['lat'],p['lat'],v['lon'],p['lon']))
    except TypeError:
        print('Not a list or not a number.')

def place(long_now, ans_me):
    """find location"""
    position_me = []
    position_me.append(long_now)
    position_me.append(ans_me)
    map = folium.Map(location=[position_me[0], position_me[1]], zoom_start=13)
    folium.Marker([position_me[0], position_me[1]], popup="Me", 
                    icon=folium.Icon(color='orange', icon="info-sign")).add_to(map)
    folium.CircleMarker(location=[position_me[0], position_me[1]], radius=60, color='blue', fill_color='green').add_to(map)

    place_nearest_hospital = []
    ord_nearest_hostipal = []

    place_police_station = []
    place_private_hospitals_no_card = []
    place_private_hospitals_card = []
    place_government_hospital_no_card = []
    place_government_hospital_card = []
    
    ord_police_station = []
    ord_private_hospitals_no_card = []
    ord_private_hospitals_card = []
    ord_government_hospital_no_card = []
    ord_government_hospital_card = []

    police_station = [
                    ['สน.ชนะสงคราม', 13.758580061361936, 100.4951217666713], 
                    ['สน.ดินแดง', 13.771372188113425, 100.5568858606255], 
                    ['สน.ดุสิต', 13.777424958083843, 100.520912154002], 
                    ['สน.นางเลิ้ง', 13.75766674276793, 100.50752034475742], 
                    ['สน.บางโพ', 13.808186702046045, 100.5188490227137], 
                    ['สน.พญาไท', 13.759408019500931, 100.53017878504497], 
                    ['สน.มักกะสัน', 13.746080973528914, 100.58360513139537], 
                    ['สน.สามเสน', 13.780709905507836, 100.50968940363404], 
                    ['สน.ห้วยขวาง', 13.777073689704363, 100.56999128710227], 
                    ['สน.คันนายาว', 13.852604640876573, 100.67006491156275], 
                    ['สน.โคกคราม', 13.830897584691318, 100.64749061028947], 
                    ['สน.ดอนเมือง', 13.934777813628552, 100.60763929168743], 
                    ['สน.เตาปูน', 13.814467693971814, 100.5314426702639], 
                    ['สน.ทุ่งสองห้อง', 13.868194213574169, 100.57124872416018], 
                    ['สน.บางเขน', 13.87510678519216, 100.5978240129355], 
                    ['สน.บางซื่อ', 13.786780900364711, 100.54740675569708], 
                    ['สน.ประชาชื่น', 13.842158583619444, 100.5468926935352], 
                    ['สน.พหลโยธิน', 13.826010783572677, 100.56966250226074], 
                    ['สน.สายไหม', 13.929256088915189, 100.66070771202712], 
                    ['สน.สุทธิสาร', 13.79161500538662, 100.57402597962864], 
                    ['สน.จรเข้น้อย', 13.718075521943115, 100.79102436674872], 
                    ['สน.ฉลองกรุง', 13.807027158112147, 100.78271708967884], 
                    ['สน.นิมิตใหม่', 13.905569052194934, 100.74844425759149], 
                    ['สน.ประชาสำราญ', 13.896800087708202, 100.86330930742842], 
                    ['สน.มีนบุรี', 13.815447460802126, 100.7349180010755], 
                    ['สน.ร่มเกล้า', 13.765898110752623, 100.73230766289923], 
                    ['สน.ลาดกระบัง', 13.721437121352887, 100.76388172247111], 
                    ['สน.ลำผักชี', 13.809461026040053, 100.8459533670448], 
                    ['สน.ลำหิน', 13.893940416502117, 100.82452847436372], 
                    ['สน.สุวินทวงศ์', 13.803691661085603, 100.92653278380658], 
                    ['สน.หนองจอก', 13.856633507623675, 100.868167523494], 
                    ['สน.โชคชัย', 13.796151607762859, 100.59339901783102],
                    ['สน.บางชัน', 13.802413568296034, 100.68624687331484],
                    ['สน.บึงกุ่ม',13.780245210557183, 100.65964848241138],
                    ['สน.ประเวศ',13.724262668057898, 100.6981045310832],
                    ['สน.วังทองหลาง', 13.759106309272314, 100.60094086634105],
                    ['สน.หัวหมาก', 13.760466440742853, 100.62724949193722],
                    ['สน.อุดมสุข', 13.67664306157995, 100.68407085552836],
                    ['สน.คลองตัน', 13.740794249165006, 100.61731736125321],
                    ['สน.ทองหล่อ', 13.73616276897007, 100.58355726630813],
                    ['สน.ท่าเรือ', 13.709320267147962, 100.58095607264771],
                    ['สน.ทุ่งมหาเมฆ', 13.718313408922091, 100.53931038251194],
                    ['สน.บางนา', 13.67418748272994, 100.64392949417702],
                    ['สน.บางโพงพาง', 13.718489982020905, 100.53923147765721],
                    ['สน.พระโขนง', 13.708657852286871, 100.59982359382504],
                    ['สน.ลุมพินี', 13.732459223272688, 100.54582183419127],
                    ['สน.วัดพระยาไกร', 13.702204313333286, 100.50264661310119],
                    ['สน.จักรวรรดิ', 13.741277936752354, 100.5022544051511],
                    ['สน.บางรัก', 13.730253454943457, 100.52327898910521],
                    ['สน.ปทุมวัน', 13.742144375517189, 100.52553186054008],
                    ['สน.พระราชวัง', 13.743188832639033, 100.49445682978578],
                    ['สน.พลับพลาไชย 2', 13.7442197921404, 100.51047922644335],
                    ['สน.ยานนาวา', 13.720524784714984, 100.51939170764253],
                    ['สน.สำราญราษฏร์', 13.75172021726872, 100.50372564870426],
                    ['สน.ตลิ่งชัน', 13.780671003243112, 100.4460644257881],
                    ['สน.ท่าพระ', 13.730078849702704, 100.4657078008824],
                    ['สน.ธรรมศาลา', 13.771127546510625, 100.35461724008888],
                    ['สน.บวรมงคล', 13.774488618290524, 100.49753541026121],
                    ['สน.บางกอกน้อย', 13.760088701318809, 100.4716142217143],
                    ['สน.บางกอกใหญ่', 13.74174450753448, 100.48670190716373],
                    ['สน.บางขุนนนท์', 13.77037431080412, 100.46828576841402],
                    ['สน.บางพลัด', 13.794939329059266, 100.490406926085],
                    ['สน.บางยี่ขัน', 13.765525100571008, 100.49144403773074],
                    ['สน.บางเสาธง', 13.74330495952257, 100.45989270637128],
                    ['สน.ศาลาแดง', 13.751502690353892, 100.35315642608464],
                    ['สน.ตลาดพลู', 13.717745081593733, 100.47401476841361],
                    ['สน.ทุ่งครุ', 13.627467397635632, 100.50694542608377],
                    ['สน.บางคอแหลม', 13.68498814188502, 100.49884502608414],
                    ['สน.บางมด', 13.673798265652515, 100.45509912608411],
                    ['สน.บางยี่เรือ', 13.726816923170212, 100.48683502793227],
                    ['สน.บุคคโล', 13.705940567056173, 100.4904913009445],
                    ['สน.บุปผาราม', 13.736351334318288, 100.48984316841373],
                    ['สน.ปากคลองสาน', 13.73116466815997, 100.50973471074299],
                    ['สน.ราษฏร์บูรณะ', 13.684124590397596, 100.49844532608418],
                    ['สน.สมเด็จเจ้าพระยา', 13.73108052373589, 100.5097568107429],
                    ['สน.สำเหร่', 13.706005627122236, 100.49055678560288],
                    ['สน.ท่าข้าม', 13.639166532736677, 100.44695868005898],
                    ['สน.เทียนทะเล', 13.551472060340851, 100.41884605491859],
                    ['สน.บางขุนเทียน', 13.68562543577415, 100.44468259909655],
                    ['สน.บางบอน', 13.645784764431928, 100.38148795491934],
                    ['สน.เพชรเกษม', 13.695914214162357, 100.3924625972489],
                    ['สน.ภาษีเจริญ', 13.715305982028582, 100.43687146841361],
                    ['สน.แสมดำ', 13.637817707125176, 100.39582400636199],
                    ['สน.หนองแขม', 13.676615490402463, 100.34551366841332],
                    ['สน.หนองค้างพลู', 13.728928957290824, 100.34905071074292],
                    ['สน.หลักสอง', 13.711555944224044, 100.38225499724904],
                    ['สน.รถไฟนพวงศ์', 13.745924733460425, 100.51675818190762],
                    ['สน.ธนบุรี', 13.759695495044227, 100.48130833957858],
                    ['สน.มักกะสัน', 13.746494861395274, 100.5834623343306],
                    ['สถานีตำรวจภูธรท่าอากาศยานสุวรรณภูมิ', 13.713781113358149, 100.775552397249]
            ]

    private_hospitals_no_card = [
                    ['โรงพยาบาลวิชัยยุทธ', 13.78314988922761, 100.53362243904631],
                    ['โรงพยาบาลเปาโล เมโมเรียล พหลโยธิน', 13.792141570393209, 100.55009495956193],
                    ['โรงพยาบาลวิภาวดี', 13.84627512442725, 100.56210780400245],
                    ['โรงพยาบาลบีแคร์ เมดิคอลเซ็นเตอร์', 13.943426265431112, 100.6245553011291],
                    ['โรงพยาบาลกรุงเทพคริสเตียน', 13.72837723462703, 100.53124494177044],
                    ['โรงพยาบาลกรุงเทพ', 13.748789423078394, 100.58322795556572],
                    ['โรงพยาบาลหัวใจ', 13.748063909909822, 100.58337273880703],
                    ['โรงพยาบาลวัฒโนสถ', 13.748372010707323, 100.58256324769923],
                    ['โรงพยาบาลบางมด 3', 13.684493820112825, 100.44414391264876],
                    ['โรงพยาบาล บางปะกอก 1', 13.67893881734407, 100.49893381954831],
                    ['โรงพยาบาล บางปะกอก-รังสิต 2', 13.99406175466883, 100.65289564089302],
                    ['โรงพยาบาลบางโพ', 13.807051534324268, 100.52329667898162],
                    ['โรงพยาบาลบีเอ็นเอช', 13.724883475672048, 100.53503133160834],
                    ['โรงพยาบาลบำรุงราษฎร์', 13.746083694345637, 100.55268790363313],
                    ['โรงพยาบาลซีจีเอช', 13.889083187338793, 100.60683534128952],
                    ['โรงพยาบาลเจ้าพระยา', 13.780458794022563, 100.47061496763814],
                    ['โรงพยาบาลคลองตัน', 13.742073921871853, 100.59454974020093],
                    ['โรงพยาบาลกรุงธน 1', 13.752767000718917, 100.47987963329156],
                    ['โรงพยาบาลนครธน', 13.660718645212466, 100.43419205471601],
                    ['โรงพยาบาลพญาไท 1', 13.756336959742134, 100.53943076995087],
                    ['โรงพยาบาลพญาไท 2', 13.77042352391289, 100.54095455405499],
                    ['โรงพยาบาลพญาไท 3', 13.723017875515826, 100.4640559053953],
                    ['โรงพยาบาลเกษมราษฎร์-บางแค', 13.710733883276799, 100.39865776430328],
                    ['โรงพยาบาลพระราม 9', 13.753089044038123, 100.57101358037839],
                    ['โรงพยาบาลรามคำแหง', 13.758159809483463, 100.63667857811234],
                    ['โรงพยาบาลจักษุรัตนิน', 13.74649372415164, 100.56301184908514],
                    ['โรงพยาบาลสมิติเวช ไชน่าทาวน์', 13.737885716129309, 100.51260249667267],
                    ['โรงพยาบาลสมิติเวชศรีนครินทร์', 13.748650742157668, 100.63868810495758],
                    ['โรงพยาบาลสมิติเวชสุขุมวิท', 13.735016603800517, 100.57656974635468],
                    ['โรงพยาบาลสมิติเวชธนบุรี', 13.714481674044949, 100.48954931189343],
                    ['โรงพยาบาลเปาโล เมโมเรียล นวมินทร์', 13.792131652609529, 100.55009500415167],
                    ['โรงพยาบาลศรีวิชัย 1', 13.776913227808606, 100.47900360544963],
                    ['โรงพยาบาลวิชัยเวช อินเตอร์เนชั่นแนล หนองแขม', 13.707488668894966, 100.36069861372073],
                    ['โรงพยาบาลเซนต์หลุยส์', 13.719138638259185, 100.52520240685969],
                    ['โรงพยาบาลสุขุมวิท', 13.718953468173217, 100.5871677416964],
                    ['โรงพยาบาลสินแพทย์', 13.678561945001789, 100.64827151613436],
                    ['โรงพยาบาลไทยนครินทร์', 13.66838627974325, 100.6385914501353],
                    ['โรงพยาบาลเทพธารินทร์', 13.714748301129326, 100.57680854016253],
                    ['โรงพยาบาลธนบุรี 1', 13.752774629036757, 100.47986845210455],
                    ['โรงพยาบาลธนบุรี 2', 13.782906365605472, 100.40042262758362],
                    ['โรงพยาบาลเวชธานี', 13.772050796198048, 100.63689228241797],
                    ['โรงพยาบาล ตาหู จมูก', 13.787606689504392, 100.47051388502723],
                    ['โรงพยาบาลกรุณาพิทักษ์', 13.708657888272024, 100.54514837236128],
                    ['โรงพยาบาลบางกอกเนอสซิ่งโฮม', 13.72468974836765, 100.53445554794231],
                    ['โรงพยาบาลยศเส', 13.74981314126488, 100.51625585079535],
                    ['โรงพยาบาลเยาวรักษ์', 13.718890890390735, 100.47242985287383],
                    ['โรงพยาบาลศูนย์มะเร็งกรุงเทพฯ', 13.779068092377353, 100.5428379581356],
                    ['โรงพยาบาลมนารมย์', 13.664745785798399, 100.60182225597646],
                    ['โรงพยาบาลลาดกระบัง เมโมเรียล', 13.741280326533206, 100.51262683561497],
                    ['โรงพยาบาลภิรมย์เภสัช', 13.75091894170405, 100.53169427669576],
                    ['โรงพยาบาลปิยะเวท', 13.753464119303146, 100.58010468676211],
                    ['โรงพยาบาลเสรีรักษ์', 13.810976098863215, 100.71687859390454],
                    ['โรงพยาบาลเสนาเวชการ', 13.831910128279036, 100.60187834008948],
                    ['โรงพยาบาลอังคทะวาณิช', 13.742691819697871, 100.51248290940478],
                    ['โรงพยาบาลจงจินต์มูลนิธิ', 13.72814027483272, 100.5407407592886],
                    ['โรงพยาบาลซังฮี้', 13.785547833407163, 100.49961780253543],
                    ['โรงพยาบาล ผิวหนัง อโศก', 13.782744492239202, 100.47304342646352],
                    ['โรงพยาบาลวิชัยเวช อินเตอร์เนชั่นแนล แยกไฟฉาย', 13.75610729682426, 100.46972673029202],
                    ['โรงพยาบาลกมล ศัลยกรรมตกแต่งและแปลงเพศ', 13.773465157917078, 100.61200251310196],
                    ['โรงพยาบาลจักษุรัตนิน', 13.746514211133748, 100.56300446252894],
                    ['โรงพยาบาลเบทเทอร์บีอิ้ง', 13.732315865883002, 100.5702986212844],
                    ['โรงพยาบาลกรุงเทพไชน่าทาวน์', 13.738078116090188, 100.51267637077254],
                    ['โรงพยาบาลเกษมราษฏร์รัตนาธิเบศร์', 13.882103141064315, 100.41041326823674],
                    ['โรงพยาบาลยันฮี', 13.799722711787872, 100.51149669591176],
                    ['โรงพยาบาลฮัมซะฮฺ', 13.860136782724819, 100.85387885358321],
                    ['โรงพยาบาลชีวา ทรานสิชั่นนัล แคร์', 13.751120685555685, 100.58334046032904],
                    ['โรงพยาบาลเอส สไปน์ แอนด์ เนิร์ฟ', 13.784643526606851, 100.60736689776003],
                    ['โรงพยาบาลผู้สูงอายุกล้วยน้ำไท 2', 13.677078741121822, 100.60699671030714],
                    ['โรงพยาบาลคามิลเลียน', 13.739532770844733, 100.58354619775969],
                    ['โรงพยาบาลบางปะกอก 9 อินเตอร์เนชั่นแนล', 13.682163148863348, 100.47443626707519],
                    ['โรงพยาบาลเกษมราษฎร์ รามคำแหง', 13.779354590736595, 100.67664512890558],
                    ['โรงพยาบาลบางขุนเทียน 1', 13.699331128308858, 100.47007088611414],
                    ['โรงพยาบาลไทยจักษุ พระราม 3', 13.709389946496026, 100.54119347126026],
                    ['โรงพยาบาลธนบุรี บำรุงเมือง', 13.750666959397117, 100.51466477846729],
                    ['โรงพยาบาลบาโนบากิ', 13.727754037634725, 100.58028328426597],
                    ['โรงพยาบาลวิมุต', 13.788978304501127, 100.54812202659559],
                    ['โรงพยาบาลมาสเตอร์พีช', 13.781102570073513, 100.51137895543106]
                                ]

    private_hospitals_card = [
                    ['โรงพยาบาลกล้วยน้ำไท', 13.713951490378227, 100.58764102608437],
                    ['โรงพยาบาลเกษมราษฏร์บางแค', 13.71060056725986, 100.39861113957818],
                    ['โรงพยาบาลเกษมราษฏร์ประชาชื่น', 13.711278631307373, 100.3986299020161],
                    ['โรงพยาบาลการุญเวช สุขาภิบาล 3', 13.776886090337445, 100.67369891074325],
                    ['โรงพยาบาลบางประกอก 3', 13.634362065126462, 100.5282707700732],
                    ['โรงพยาบาลนวมินทร์', 13.81126094659419, 100.72160479973105],
                    ['โรงพยาบาลนวมินทร์ 9', 13.811266771678644, 100.72400432608511],
                    ['โรงพยาบาลบางนา 1', 13.666845740528974, 100.63549846841323],
                    ['โรงพยาบาลบางประกอก 8', 13.663194890411077, 100.40692139724861],
                    ['โรงพยาบาลบางไผ่', 13.725069057807907, 100.46490763957826],
                    ['โรงพยาบาลบางมด', 13.67178691524675, 100.45650145491945],
                    ['โรงพยาบาลบี.แคร์ เมดิคอลเซ็นเตอร์', 13.943385290229951, 100.62454449725074],
                    ['โรงพยาบาล​ ไอเอ็มเอช ธนบุรี', 13.67773751329529, 100.49855776841333],
                    ['โรงพยาบาลเปาโล โชคชัย 4', 13.801948466537985, 100.59612653957879],
                    ['โรงพยาบาลเปาโล เกษตร', 13.835406272743054, 100.57418679724987],
                    ['โรงพยาบาลพีเอ็มจี', 13.651698390418572, 100.42200169724848],
                    ['โรงพยาบาลเพชรเวช', 13.742719133747755, 100.59481913957843],
                    ['โรงพยาบาลแพทย์ปัญญา', 13.743914933640571, 100.60743119724921],
                    ['โรงพยาบาลมเหสักข์', 13.725444435294948, 100.51958453957829],
                    ['โรงพยาบาลมงกุฎวัฒนะ', 13.893998390261816, 100.56163822608568],
                    ['โรงพยาบาลมิชชั่น', 13.757857369330269, 100.51948086841396],
                    ['โรงพยาบาลราษฎร์บูรณะ', 13.677932839540262, 100.50281661074249],
                    ['โรงพยาบาลลาดพร้าว', 13.778503390336377, 100.62375309724946],
                    ['โรงพยาบาลวิภาราม', 13.73541501974609, 100.64496209507911],
                    ['โรงพยาบาลศิครินทร์', 13.654954564405495, 100.64638208929074],
                    ['โรงพยาบาลซีจีเอช สายไหม', 13.924195017380304, 100.68416429725055],
                    ['โรงพยาบาลสุขสวัสดิ์', 13.676139565051276, 100.50109651841338],
                    ['โรงพยาบาลหัวเฉียว', 13.750061447621912, 100.51543355492001],
                            ]

    government_hospital_no_card =  [
                    ['โรงพยาบาลเวชศาสตร์เขตร้อน', 13.76649105447018, 100.53369148544702],
                    ['โรงพยาบาลนวุติสมเด็จย่า', 13.766579335873553, 100.53369517204472],
                    ['โรงพยาบาลประสานมิตร',13.784915370187294, 100.54608004374747],
                    ['โรงพยาบาลทหารเรือกรุงเทพ',13.670523482387296, 100.58780879300501],
                    ['โรงพยาบาลมูลนิธิมิราเคิล ออฟไลฟ์', 13.815747500704568, 100.55264452094978],
                    ['โรงพยาบาลจุฬาภรณ์', 13.880987127564298, 100.57813778623867],
                    ['โรงพยาบาลศิริราช ปิยมหาราชการุณย์', 13.759892180046903, 100.48561871801977],
                    ['โรงพยาบาลพระจอมเกล้าเจ้าคุณทหาร', 13.73210692808113, 100.78866864683717],
                    ['โรงพยาบาลการไฟฟ้านครหลวง', 13.786983893062361, 100.5096671890691],
                    ['โรงพยาบาลชลประทาน มหาวิทยาลัยศรีนครินทรวิโรฒ', 13.897982047938832, 100.5039495106583],
                    ['โรงพยาบาลสวนเบญจกิติเฉลิมพระเกียรติ 84 พรรษา', 13.724696338304476, 100.55397794329528],
                    ['โรงพยาบาลคลองสามวา',13.91022553533959, 100.75369340893728]
                                   ]
   
    government_hospital_card = [
                    ['โรงพยาบาลจุฬาลงกรณ์', 13.730875834858033, 100.53631682479514],
                    ['โรงพยาบาลตำรวจ', 13.742905730864631, 100.53854193535399],
                    ['โรงพยาบาลนพรัตนราชธานี', 13.817718140966067, 100.68806138431741],
                    ['โรงพยาบาลพระมงกุฎเกล้า', 13.76758059916482, 100.53410204410945],
                    ['โรงพยาบาลภูมิพลอดุลยเดช', 13.909449260749414, 100.61785358246819],
                    ['โรงพยาบาลราชวิถี', 13.854402102602002, 100.52762248555935],
                    ['โรงพยาบาลรามาธิบดี', 13.766974451993438, 100.52661916682415],
                    ['โรงพยาบาลเลิดสิน', 13.722269565545751, 100.5173887845215],
                    ['โรงพยาบาลศิริราช', 13.760080568062355, 100.48564368768918],
                    ['โรงพยาบาลสมเด็จพระปิ่นเกล้า', 13.710142415907994, 100.48683592000104],
                    ['โรงพยาบาลเทียนฟ้า มูลนิธิ', 13.738237016248421, 100.5121702401381],
                    ['คณะแพทยศาสตร์วชิรพยาบาล มหาวิทยาลัยนวมินทราธิราช', 13.780707898507833, 100.50917528275816],
                    ['โรงพยาบาลกลาง', 13.746695186195582, 100.50923646714725],
                    ['โรงพยาบาลเจริญกรุงประชารักษ์', 13.694503434397468, 100.49465715194017],
                    ['โรงพยาบาลตากสิน', 13.730922340313976, 100.50857217933655],
                    ['โรงพยาบาลราชพิพัฒน์', 13.731001840181596, 100.36682586982458],
                    ['โรงพยาบาลเวชการุณย์รัศมิ์', 13.85681310297025, 100.85900475942876],
                    ['โรงพยาบาลสิรินธร', 13.717533815750283, 100.70591549575649],
                    ['โรงพยาบาลลาดกระบังกรุงเทพมหานคร', 13.722509831530713, 100.78413732650195]
                               ]
    
    #มาคจุดต่างๆ
    for loc_police_station in police_station:
        folium.Marker([loc_police_station[1], loc_police_station[2]], popup=loc_police_station[0],
                    icon=folium.Icon(color='gray', icon="hdd")).add_to(map)
        place_police_station.append({'type': 'FeatureCollection',
        'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [loc_police_station[1], loc_police_station[2]]}}]})

    for loc_pv_hospi_no_card in private_hospitals_no_card:
        folium.Marker([loc_pv_hospi_no_card[1], loc_pv_hospi_no_card[2]], 
                    popup=loc_pv_hospi_no_card[0], icon=folium.Icon(color='red', icon_color='white', prefix='fa', icon='plus')).add_to(map)
        place_private_hospitals_no_card.append({'type': 'FeatureCollection',
        'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [loc_pv_hospi_no_card[1], loc_pv_hospi_no_card[2]]}}]})

    for loc_pv_hospi_card in private_hospitals_card:
        folium.Marker([loc_pv_hospi_card[1], loc_pv_hospi_card[2]], 
                    popup=loc_pv_hospi_card[0], icon=folium.Icon(color='cadetblue', icon="plus")).add_to(map)
        place_private_hospitals_card.append({'type': 'FeatureCollection',
        'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [loc_pv_hospi_card[1], loc_pv_hospi_card[2]]}}]})

    for loc_gm_hospi_no_card in government_hospital_no_card:
        folium.Marker([loc_gm_hospi_no_card[1], loc_gm_hospi_no_card[2]], 
                    popup=loc_gm_hospi_no_card[0], icon=folium.Icon(color='blue', icon="plus")).add_to(map)
        place_government_hospital_no_card.append({'type': 'FeatureCollection',
        'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [loc_gm_hospi_no_card[1], loc_gm_hospi_no_card[2]]}}]})
    
    for loc_gm_hospi_card in government_hospital_card:
        folium.Marker([loc_gm_hospi_card[1], loc_gm_hospi_card[2]], 
                    popup=loc_gm_hospi_card[0], icon=folium.Icon(color='green', icon="plus")).add_to(map)
        place_government_hospital_card.append({'type': 'FeatureCollection',
        'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [loc_gm_hospi_card[1], loc_gm_hospi_card[2]]}}]})
   
    #หาพิกัดของโรงพยาบาล
    point_to_find = {'lat': position_me[0], 'lon': position_me[1]} #ตำแหน่งของเรา
    for answer_ps in place_police_station:
        if answer_ps['features']:
            lat = answer_ps['features'][0]['geometry']['coordinates'][0]
            lon = answer_ps['features'][0]['geometry']['coordinates'][1]

            temp_place_police_station = {'lat': lat, 'lon': lon}
            ord_police_station.append(temp_place_police_station)
            ans_police = find_closest_lat_lon(ord_police_station, point_to_find)
    
    for answer_ph_no_c in place_private_hospitals_no_card:
        if answer_ph_no_c['features']:
            lat = answer_ph_no_c['features'][0]['geometry']['coordinates'][0]
            lon = answer_ph_no_c['features'][0]['geometry']['coordinates'][1]

            temp_place_private_hospitals_no_card = {'lat': lat, 'lon': lon}
            ord_private_hospitals_no_card.append(temp_place_private_hospitals_no_card)
            ans_private_hospitals_no_card = find_closest_lat_lon(ord_private_hospitals_no_card, point_to_find)

    for answer_phc in place_private_hospitals_card:
        if answer_phc['features']:
            lat = answer_phc['features'][0]['geometry']['coordinates'][0]
            lon = answer_phc['features'][0]['geometry']['coordinates'][1]

            temp_place_private_hospitals_card = {'lat': lat, 'lon': lon}
            ord_private_hospitals_card.append(temp_place_private_hospitals_card)
            ans_private_hospitals_card = find_closest_lat_lon(ord_private_hospitals_card, point_to_find)
    
    for answer_gh_no_c in place_government_hospital_no_card:
        if answer_gh_no_c['features']:
            lat = answer_gh_no_c['features'][0]['geometry']['coordinates'][0]
            lon = answer_gh_no_c['features'][0]['geometry']['coordinates'][1]

            temp_place_government_hospital_no_card = {'lat': lat, 'lon': lon}
            ord_government_hospital_no_card.append(temp_place_government_hospital_no_card)
            ans_government_hospital_no_card = find_closest_lat_lon(ord_government_hospital_no_card, point_to_find)
    
    for answer_ghc in place_government_hospital_card:
        if answer_ghc['features']:
            lat = answer_ghc['features'][0]['geometry']['coordinates'][0]
            lon = answer_ghc['features'][0]['geometry']['coordinates'][1]

            temp_place_government_hospital_card = {'lat': lat, 'lon': lon}
            ord_government_hospital_card.append(temp_place_government_hospital_card)
            ans_government_hospital_card = find_closest_lat_lon(ord_government_hospital_card, point_to_find)
    
    #หาจาก lat เเละ lon ว่า โรงพยาบาลคืออะไร
    for find_police_station in police_station:
        if ans_police["lat"] == find_police_station[1]:
            folium.CircleMarker(location=[find_police_station[1], find_police_station[2]], radius=60, color='red', fill_color='pink').add_to(map)
            route_lats_longs = [[position_me[0], position_me[1]], [find_police_station[1], find_police_station[2]]]
            plugins.AntPath(route_lats_longs).add_to(map)

    for find_private_hospitals_no_card in private_hospitals_no_card:
        if ans_private_hospitals_no_card["lat"] == find_private_hospitals_no_card[1]:
            folium.CircleMarker(location=[find_private_hospitals_no_card[1], find_private_hospitals_no_card[2]], radius=60, color='purple', fill_color='gray').add_to(map)
            place_nearest_hospital.append({'type': 'FeatureCollection',
                    'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [find_private_hospitals_no_card[1], find_private_hospitals_no_card[2]]}}]})

    for find_private_hospitals_card in private_hospitals_card:
        if ans_private_hospitals_card["lat"] == find_private_hospitals_card[1]:
            folium.CircleMarker(location=[find_private_hospitals_card[1], find_private_hospitals_card[2]], radius=60, color='purple', fill_color='gray').add_to(map)
            place_nearest_hospital.append({'type': 'FeatureCollection',
                    'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [find_private_hospitals_card[1], find_private_hospitals_card[2]]}}]})
    
    for find_government_hospital_no_card in government_hospital_no_card:
        if ans_government_hospital_no_card["lat"] == find_government_hospital_no_card[1]:
            folium.CircleMarker(location=[find_government_hospital_no_card[1], find_government_hospital_no_card[2]], radius=60, color='purple', fill_color='gray').add_to(map)
            place_nearest_hospital.append({'type': 'FeatureCollection',
                    'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [find_government_hospital_no_card[1], find_government_hospital_no_card[2]]}}]})
    
    for find_government_hospital_card in government_hospital_card:
        if ans_government_hospital_card["lat"] == find_government_hospital_card[1]:
            folium.CircleMarker(location=[find_government_hospital_card[1], find_government_hospital_card[2]], radius=60, color='purple', fill_color='gray').add_to(map)
            place_nearest_hospital.append({'type': 'FeatureCollection',
                    'query': [0, 0], 'features': [{'geometry': {'type': 'Point', 'coordinates': [find_government_hospital_card[1], find_government_hospital_card[2]]}}]})
    
    #หาที่ใกล้ที่สุดกันจริงๆ
    for answer_nearest_hostipal in place_nearest_hospital:
        if answer_nearest_hostipal['features']:
            lat = answer_nearest_hostipal['features'][0]['geometry']['coordinates'][0]
            lon = answer_nearest_hostipal['features'][0]['geometry']['coordinates'][1]

            temp_nearest_hostipal = {'lat': lat, 'lon': lon}
            ord_nearest_hostipal.append(temp_nearest_hostipal)
            ans_nearest_hostipal = find_closest_lat_lon(ord_nearest_hostipal, point_to_find)
    
    #เปลี่ยนสีที่โรงพยาบาลที่ใกล้ที่สุด   
    for find_nearest_private_hospitals_no_card in private_hospitals_no_card:
        if ans_nearest_hostipal["lat"] == find_nearest_private_hospitals_no_card[1]:
            folium.CircleMarker(location=[find_nearest_private_hospitals_no_card[1], find_nearest_private_hospitals_no_card[2]], radius=60, color='red', fill_color='pink').add_to(map)
            route_lats_longs = [[position_me[0], position_me[1]], [find_nearest_private_hospitals_no_card[1], find_nearest_private_hospitals_no_card[2]]]
            plugins.AntPath(route_lats_longs).add_to(map)

    for find_nearest_private_hospitals_card in private_hospitals_card:
        if ans_nearest_hostipal["lat"] == find_nearest_private_hospitals_card[1]:
            folium.CircleMarker(location=[find_nearest_private_hospitals_card[1], find_nearest_private_hospitals_card[2]], radius=60, color='red', fill_color='pink').add_to(map)
            route_lats_longs = [[position_me[0], position_me[1]], [find_nearest_private_hospitals_card[1], find_nearest_private_hospitals_card[2]]]
            plugins.AntPath(route_lats_longs).add_to(map)

    for find_nearest_government_hospital_no_card in government_hospital_no_card:
        if ans_nearest_hostipal["lat"] == find_nearest_government_hospital_no_card[1]:
            folium.CircleMarker(location=[find_nearest_government_hospital_no_card[1], find_nearest_government_hospital_no_card[2]], radius=60, color='red', fill_color='pink').add_to(map)
            route_lats_longs = [[position_me[0], position_me[1]], [find_nearest_government_hospital_no_card[1], find_nearest_government_hospital_no_card[2]]]
            plugins.AntPath(route_lats_longs).add_to(map)

    for find_nearest_government_hospital_card in government_hospital_card:
        if ans_nearest_hostipal["lat"] == find_nearest_government_hospital_card[1]:
            folium.CircleMarker(location=[find_nearest_government_hospital_card[1], find_nearest_government_hospital_card[2]], radius=60, color='red', fill_color='pink').add_to(map)
            route_lats_longs = [[position_me[0], position_me[1]], [find_nearest_government_hospital_card[1], find_nearest_government_hospital_card[2]]]
            plugins.AntPath(route_lats_longs).add_to(map)
    map.save("emergency_map.html")

def main():
    """main"""
    long = float(input())
    ans = float(input())
    place(long, ans)
main()
