"""Create original, accessible, dependency-free SVG teaching diagrams."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets"
INK = "#172b4d"

def start(title, desc, height):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="{height}" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">',
            f'<title id="title">{escape(title)}</title><desc id="desc">{escape(desc)}</desc>',
            '<defs><marker id="arrow" markerWidth="9" markerHeight="9" refX="7" refY="4" orient="auto"><path d="M0 0 L8 4 L0 8 Z" fill="#53657d"/></marker></defs>',
            f'<rect width="1200" height="{height}" fill="#f7f9fc"/>',
            '<g font-family="Arial, Helvetica, sans-serif" fill="#172b4d">']

def text(parts, x, y, value, size=20, weight="400", color=INK):
    parts.append(f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{color}">{escape(value)}</text>')

def box(parts, x, y, w, h, title, lines, fill="#ffffff", accent="#377cf6"):
    parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="#d7e0eb"/>')
    parts.append(f'<rect x="{x}" y="{y+16}" width="5" height="{h-32}" rx="2" fill="{accent}"/>')
    text(parts,x+22,y+37,title,22,"700")
    for i,line in enumerate(lines):
        text(parts,x+22,y+69+i*26,line,18,color="#455b75")

def arrow(parts, path):
    parts.append(f'<path d="{path}" fill="none" stroke="#53657d" stroke-width="2.5" marker-end="url(#arrow)"/>')

def save(name, p):
    OUT.mkdir(exist_ok=True)
    (OUT/name).write_text("\n".join(p+["</g></svg>"]))

def loop():
    p=start("World models for reinforcement learning", "Experience trains a predictive model. The model supports online planning or imagined actor learning. Actions return to the environment.", 670)
    text(p,45,54,"WORLD MODELS FOR REINFORCEMENT LEARNING",15,"700","#3a6fad")
    text(p,45,99,"Predict action consequences. Improve decisions.",34,"700")
    text(p,45,133,"A model is one component of a learning-and-control loop.",20,color="#53657d")
    box(p,45,200,250,145,"Environment",["Take action a(t)","Observe o(t+1), r(t)"],"#eaf2ff")
    box(p,360,200,320,145,"Experience + state",["Store action trajectories", "Infer z(t) from history"],"#ffffff")
    box(p,750,200,405,145,"Learned world model",["Given z(t) and candidate a(t)","predict z(t+1), reward / features"],"#e9f7f2", "#168b6c")
    arrow(p,"M295 267 H350"); arrow(p,"M680 267 H740")
    box(p,360,430,355,145,"Online planning",["Compare candidate action plans", "Execute first action; replan"],"#fff5e8","#bd7920")
    box(p,785,430,370,145,"Policy learning",["Train actor in imagined rollouts", "Use actor to select actions"],"#f0edff","#7854bb")
    arrow(p,"M850 345 V389 H540 V420"); arrow(p,"M970 345 V420")
    arrow(p,"M360 502 H170 V355")
    arrow(p,"M970 575 V614 H170 V355")
    text(p,54,484,"actions",18,"700")
    text(p,45,651,"Original schematic • Some methods combine both routes; tree search is another model-use pattern.",17,color="#53657d")
    save("world-model-loop.svg",p)

def paths():
    p=start("Three ways to use a learned world model", "Online planning optimizes action sequences; imagination trains an actor; tree search uses reward, value and policy predictions.",700)
    text(p,45,55,"FROM PREDICTION TO ACTION",15,"700","#3a6fad")
    text(p,45,102,"Where does the decision computation happen?",33,"700")
    rows=[(155,"01  Online planning","PlaNet / TD-MPC",["Infer current state","Roll out action plans","Score and act"],"#fff5e8"),
          (320,"02  Imagination","Dreamer (through V3)",["Seed model rollouts","Train actor + critic","Deploy actor"],"#f0edff"),
          (485,"03  Tree search","MuZero",["Encode observation","Expand search tree","Choose action"],"#e9f7f2")]
    for y,title,method,stages,fill in rows:
        text(p,45,y+25,title,23,"700"); text(p,45,y+58,method,17,color="#53657d")
        for i,stage in enumerate(stages):
            x=340+280*i
            box(p,x,y-10,255,102,stage if len(stage)<23 else stage.split(" + ")[0],[],fill)
            # Short subtitles clarify deployment and the combined last stage.
            subtitle = ["Real observations", "Hypothetical futures", "Action selection"][i]
            if title.startswith("02"):
                subtitle=["Training", "Training", "Decision time"][i]
            text(p,x+22,y+62,subtitle,17,color="#53657d")
            if i<2: arrow(p,f"M{x+255} {y+40} H{x+272}")
    text(p,45,660,"Original schematic • An actor head may also guide MPC or tree search; these are not exclusive categories.",17,color="#53657d")
    save("decision-paths.svg",p)

def space():
    p=start("Two independent design axes", "Prediction targets are observations, embeddings, or decision quantities. These combine with online planning, actor learning, and search.",655)
    text(p,45,55,"A MAP OF DESIGN CHOICES",15,"700","#3a6fad")
    text(p,45,102,"What is learned? How is it used?",34,"700")
    text(p,45,137,"Illustrative families, not a performance ranking or exhaustive taxonomy.",20,color="#53657d")
    xs=[340,615,890]
    for x,label in zip(xs,["Online trajectory planning","Actor learning in imagination","Tree search"]):
        text(p,x,193,label,17,"700")
    names=[("Reconstruction + dynamics",["PlaNet","Dreamer through V3","—"]),
           ("Future embeddings",["DINO-WM / V-JEPA 2-AC","Possible combination","Possible combination"]),
           ("Task / decision objectives",["TD-MPC / TD-MPC2","Possible combination","MuZero"])]
    for i,(label,cells) in enumerate(names):
        y=225+i*115
        text(p,45,y+44,label,20,"700")
        for x,cell in zip(xs,cells):
            p.append(f'<rect x="{x-12}" y="{y}" width="262" height="88" rx="12" fill="{["#eaf2ff","#e9f7f2","#fff5e8"][i]}"/>')
            text(p,x+1,y+49,cell,17,"400")
    text(p,45,605,"Original schematic • TD-MPC also uses embedding consistency; rows describe emphasis, not disjoint losses.",17,color="#53657d")
    save("design-space.svg",p)

if __name__ == "__main__":
    loop(); paths(); space()
    print("Generated three original SVG diagrams.")
