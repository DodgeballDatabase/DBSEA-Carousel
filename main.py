from dataclasses import dataclass

print_to_console = True

amber_filter = "has-luminous-vivid-amber-background-color"
amber_top_line = "#ff6900"
amber_duotone = "wp-duotone-cf2e2e-fcb900-1"

green_filter = "has-vivid-green-cyan-background-color"
green_top_line = "#7bdcb5"

pink_filter = "has-pale-pink-background-color"

red_filter = "has-vivid-red-background-color"

blue_filter = "has-vivid-cyan-blue-background-color"

light_gray_filter = "has-very-light-gray-background-color"

orange_filter = "has-luminous-vivid-orange-background-color"

purple_top_line = "#9b51e0"

rainbow_comp_custom_duotone = "wp-duotone-rgb19975221-rgb253186204-2"


@dataclass
class Instance:
    top_line: str
    mid_line: str
    bot_line: str
    link: str
    img_src: str
    wp_image_num: str
    text_color_class: str
    background_color: str
    top_line_background_color: str
    duotone: str
    object_position: str
    dim: int = 0 # 0-100: 0 is fully transparent, 100 is fully opaque, increments of 10
    has_bg_dim: bool = True
    svg: str = ""

def get_social_league_instance():
    top_line = "Fall Social League"
    mid_line = "Sunday, 5-7 PM"
    bot_line = "Garfield Community Center"

    link = "https://www.dodgeballseattle.com/social-league-fall-2024"
    img_src = "https://www.dodgeballseattle.com/wp-content/uploads/2022/10/homepage.jpg"
    wp_image_num = "wp-image-5451"
    text_color_class = "has-white-color"

    background_color = amber_filter
    top_line_background_color = amber_top_line
    duotone = amber_duotone

    object_position = "object-position:44% 0%"

    dim = 70

    svg = "svg-social.html"

    return Instance(top_line, mid_line, bot_line, link, img_src, wp_image_num, text_color_class, background_color, top_line_background_color, duotone, object_position, dim, svg=svg)

def get_rainbow_league_instance():
    top_line = "Fall Rainbow League"
    mid_line = "Wednesdays, 7-9 PM"
    bot_line = "Yesler Community Center"

    link = "https://www.dodgeballseattle.com/rainbow-league-fall-2024/"
    img_src = "https://www.dodgeballseattle.com/wp-content/uploads/2022/05/summer-rainbow.jpg"
    wp_image_num = "wp-image-6381"
    text_color_class = "has-white-color"

    background_color = ""
    top_line_background_color = purple_top_line
    duotone = ""

    object_position = ""

    dim = 40

    return Instance(top_line, mid_line, bot_line, link, img_src, wp_image_num, text_color_class, background_color, top_line_background_color, duotone, object_position, dim)

def get_squid_instance():
    top_line = ""
    mid_line = ""
    bot_line = ""

    link = "https://www.dodgeballseattle.com/squid-2024-seattle-queer-international-dodgeball-open"
    img_src = "https://www.dodgeballseattle.com/wp-content/uploads/2024/05/FB_BANNER_SQ2.png"
    wp_image_num = "wp-image-7713"
    text_color_class = "has-white-color"

    background_color = ""
    top_line_background_color = ""
    duotone = ""

    object_position = ""

    return Instance(top_line, mid_line, bot_line, link, img_src, wp_image_num, text_color_class, background_color, top_line_background_color, duotone, object_position, has_bg_dim=False)

def get_dei_instance():
    top_line = ""
    mid_line = ""
    bot_line = ""

    link = "https://www.dodgeballseattle.com/diversity-equity-inclusion-statement/"
    img_src = "https://www.dodgeballseattle.com/wp-content/uploads/2021/01/dbsea-org-dei-statement2.png"
    wp_image_num = "wp-image-5522"
    text_color_class = ""

    background_color = ""
    top_line_background_color = ""
    duotone = ""

    object_position = ""

    return Instance(top_line, mid_line, bot_line, link, img_src, wp_image_num, text_color_class, background_color, top_line_background_color, duotone, object_position, has_bg_dim=False)

def get_rainbow_comp_league_instance():
    top_line = "Fall Rainbow Competitive League"
    mid_line = "Sundays, 7-9 PM"
    bot_line = "Garfield Community Center"

    link = "https://www.dodgeballseattle.com/rainbow-competitive-league-fall-2024/"
    img_src = "http://www.dodgeballseattle.com/wp-content/uploads/2022/06/270647771_629299375003255_2569366123279748269_n-edited-scaled-e1656539835783.jpg"
    wp_image_num = "wp-image-6513"
    text_color_class = "has-white-color"

    background_color = ""
    top_line_background_color = "#5a1a97"
    duotone = rainbow_comp_custom_duotone

    object_position = "object-position:44% 0%"

    dim = 0

    svg = "svg-rainbow-comp.html"

    return Instance(top_line, mid_line, bot_line, link, img_src, wp_image_num, text_color_class, background_color,
                    top_line_background_color, duotone, object_position, dim, svg=svg)

def get_comp_league_instance():
    top_line = "Comp League"
    mid_line = "Mondays, 7-9 PM"
    bot_line = "Yesler Community Center"

    link = "https://www.dodgeballseattle.com/competitive-foam-league-summer-2024/"
    img_src = "https://www.dodgeballseattle.com/wp-content/uploads/2022/05/summer-comp.jpg"
    wp_image_num = "wp-image-6379"
    text_color_class = "has-white-color"

    background_color = ""
    top_line_background_color = "#791c1c"
    duotone = ""

    object_position = "object-position:47% 0%"

    dim = 20

    return Instance(top_line, mid_line, bot_line, link, img_src, wp_image_num, text_color_class, background_color,
                    top_line_background_color, duotone, object_position, dim)

def generate(slide_instance: Instance, name: str) -> str:

    tl_bg_color = ""
    if slide_instance.top_line_background_color != "":
        tl_bg_color = f"background-color:{slide_instance.top_line_background_color}"

    bg_color = ""
    if slide_instance.background_color != "":
        bg_color = f"{slide_instance.background_color}"

    if slide_instance.dim > 0:
        bg_color += f" has-background-dim-{slide_instance.dim} has-background"

    if slide_instance.has_bg_dim:
        bg_color += " has-background-dim"

    svg = ""
    if slide_instance.svg != "":
        with open(slide_instance.svg, 'r') as svg_file:
            svg = svg_file.read()

    text = f"""
<div class="wp-block-cover is-style-editorskit-rounded ek-linked-block {slide_instance.duotone}" style="min-height:350px;aspect-ratio:unset;">
    <span aria-hidden="false" class="wp-block-cover__background {bg_color}"></span>
    <img decoding="async" class="wp-block-cover__image-background {slide_instance.wp_image_num} ls-is-cached lazyloaded" alt="" src="{slide_instance.img_src}" data-src="{slide_instance.img_src}" style="{slide_instance.object_position}" data-object-fit="cover" data-object-position="{slide_instance.object_position}">
    <div class="wp-block-cover__inner-container is-layout-flow wp-block-cover-is-layout-flow">
        <p class="has-text-align-center has-large-font-size {slide_instance.text_color_class} has-text-color">
            <strong>
                <span style="{tl_bg_color}" class="has-inline-background">{slide_instance.top_line}</span>
            </strong>
            <br/>
            {slide_instance.mid_line}
            <br/>
            {slide_instance.bot_line}
        </p>
    </div>
    <a href="{slide_instance.link}" class="editorskit-block-link" rel=""></a>
</div>
{svg}
"""

    if print_to_console:
        print()
        print(name)
        print("=====================================")
        print(text)
    return text

def write_to_file(slide_str: str):
    with open('template.html', 'r') as template:
        template_text = template.read()
        with open('flat_preview.html', 'w+') as out_file:
            out_file.write(template_text.replace("{SLIDES}", slide_str))

slides = ""
slides += generate(get_squid_instance(), "Squid 2024")
slides += generate(get_social_league_instance(), "Social League")
slides += generate(get_rainbow_league_instance(), "Rainbow League")
slides += generate(get_rainbow_comp_league_instance(), "Rainbow Comp League")
slides += generate(get_comp_league_instance(), "Comp League")
slides += generate(get_dei_instance(), "DEI")

write_to_file(slides)
