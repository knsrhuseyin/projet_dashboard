from itertools import product

# -------------------
# Définition des utilitaires
# -------------------
colors = ["red","blue","green","yellow","gray","pink","purple","indigo","orange","teal","lime","cyan","rose","fuchsia","violet","sky","emerald","amber","lime","stone"]
intensities = [50,100,200,300,400,500,600,700,800,900]

spacings = list(range(0,65))
font_sizes = ["xs","sm","base","lg","xl","2xl","3xl","4xl","5xl","6xl","7xl","8xl","9xl"]
font_weights = ["thin","extralight","light","normal","medium","semibold","bold","extrabold","black"]
rounded = ["none","sm","md","lg","xl","2xl","3xl","full"]
shadow = ["sm","md","lg","xl","2xl","inner","none"]
opacity = list(range(0,101,5))
flex_items = ["start","center","end","baseline","stretch"]
flex_justify = ["start","center","end","between","around","evenly"]
grid_cols = list(range(1,13))
grid_rows = list(range(1,7))
ring_widths = [0,1,2,4,8]
ring_offsets = [0,1,2,4,8]
blur_values = ["sm","md","lg","xl","2xl","3xl","none","0"]
scale_values = [50,75,90,95,100,105,110,125,150]
rotate_values = [0,1,2,3,6,12,45,90,180]
translate_values = [0,1,2,3,4,5,6,8,10,12,16,20,24,32,40,48,56,64]
skew_values = [0,1,2,3,6,12]
motion = ["animate-none","animate-spin","animate-ping","animate-pulse","animate-bounce"]
transition = ["transition","transition-all","transition-colors","transition-opacity","transition-shadow","transition-transform"]
duration = [75,100,150,200,300,500,700,1000]
ease = ["linear","in","out","in-out"]
backdrop_filters = ["backdrop-blur-sm","backdrop-blur-md","backdrop-blur-lg","backdrop-blur-xl","backdrop-blur-2xl","backdrop-blur-3xl","backdrop-brightness-0","backdrop-brightness-50","backdrop-brightness-75","backdrop-brightness-90","backdrop-brightness-95","backdrop-brightness-100","backdrop-brightness-105","backdrop-brightness-110"]

pseudo_states = ["hover","focus","active","disabled","visited","first","last","odd","even","checked","focus-within","focus-visible"]
screen_sizes = ["sm","md","lg","xl","2xl"]
dark_mode = ["dark"]

# -------------------
# Fonction pour combiner préfixes
# -------------------
def apply_variants(base_classes):
    all_classes = set()
    for cls in base_classes:
        all_classes.add(cls)
        # pseudo-classes
        for state in pseudo_states:
            all_classes.add(f"{state}:{cls}")
        # responsive
        for screen in screen_sizes:
            all_classes.add(f"{screen}:{cls}")
            for state in pseudo_states:
                all_classes.add(f"{screen}:{state}:{cls}")
        # dark mode
        for d in dark_mode:
            all_classes.add(f"{d}:{cls}")
            for state in pseudo_states:
                all_classes.add(f"{d}:{state}:{cls}")
            for screen in screen_sizes:
                all_classes.add(f"{screen}:{d}:{cls}")
                for state in pseudo_states:
                    all_classes.add(f"{screen}:{d}:{state}:{cls}")
    return all_classes

# -------------------
# Génération des classes
# -------------------
all_classes = set()

# couleurs
for color,intensity in product(colors,intensities):
    all_classes.update(apply_variants([
        f"text-{color}-{intensity}",
        f"bg-{color}-{intensity}",
        f"border-{color}-{intensity}",
        f"ring-{color}-{intensity}",
        f"placeholder-{color}-{intensity}",
        f"caret-{color}-{intensity}"
    ]))

# spacing
for s in spacings:
    all_classes.update(apply_variants([
        f"m-{s}", f"mt-{s}", f"mb-{s}", f"ml-{s}", f"mr-{s}",
        f"mx-{s}", f"my-{s}",
        f"p-{s}", f"pt-{s}", f"pb-{s}", f"pl-{s}", f"pr-{s}",
        f"px-{s}", f"py-{s}",
        f"gap-{s}", f"space-x-{s}", f"space-y-{s}"
    ]))

# typo
for size in font_sizes:
    all_classes.update(apply_variants([f"text-{size}"]))
for weight in font_weights:
    all_classes.update(apply_variants([f"font-{weight}"]))
all_classes.update(apply_variants(["italic","not-italic","uppercase","lowercase","capitalize"]))

# border & rounding
all_classes.update(apply_variants([
    "border","border-0","border-2","border-4","border-8",
    "rounded","rounded-t","rounded-b","rounded-l","rounded-r",
    "rounded-tl","rounded-tr","rounded-bl","rounded-br"
]))
for r in rounded:
    all_classes.update(apply_variants([f"rounded-{r}"]))
for s in shadow:
    all_classes.update(apply_variants([f"shadow-{s}"]))
for o in opacity:
    all_classes.update(apply_variants([f"opacity-{o}"]))

# flex/grid
all_classes.update(apply_variants(["flex","flex-row","flex-col","flex-wrap","flex-nowrap","grid"]))
for item in flex_items:
    all_classes.update(apply_variants([f"items-{item}"]))
for j in flex_justify:
    all_classes.update(apply_variants([f"justify-{j}"]))
for c in grid_cols:
    all_classes.update(apply_variants([f"grid-cols-{c}"]))
for r in grid_rows:
    all_classes.update(apply_variants([f"grid-rows-{r}"]))

# transform
for s in scale_values:
    all_classes.update(apply_variants([f"scale-{s}"]))
for r in rotate_values:
    all_classes.update(apply_variants([f"rotate-{r}"]))
for t in translate_values:
    all_classes.update(apply_variants([f"translate-x-{t}", f"translate-y-{t}"]))
for k in skew_values:
    all_classes.update(apply_variants([f"skew-x-{k}", f"skew-y-{k}"]))

# ring & outline
for w in ring_widths:
    all_classes.update(apply_variants([f"ring-{w}"]))
for o in ring_offsets:
    all_classes.update(apply_variants([f"ring-offset-{o}"]))

# motion & transition
all_classes.update(apply_variants(motion))
all_classes.update(apply_variants(transition))
for d in duration:
    all_classes.update(apply_variants([f"duration-{d}"]))
for e in ease:
    all_classes.update(apply_variants([f"ease-{e}"]))

# filters
all_classes.update(apply_variants(blur_values))
all_classes.update(apply_variants(backdrop_filters))

# -------------------
# Génération HTML final
# -------------------
with open("templates/html/generate_class.html","w") as f:
    f.write('<div class="\n')
    for cls in sorted(all_classes):
        f.write(f'  {cls}\n')
    f.write('"></div>\n')

print(f"[💣] Généré avec {len(all_classes)} classes dans templates/html/generate_class.html")
