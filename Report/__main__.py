import click
from .Recorder import lookup
from .Recorder import detailed_info


def overall_report():
    info = lookup()
    click.echo(click.style('2019-nCoV病毒目前在中国的传播数据如下：', fg='blue'))
    click.echo('确诊：' + click.style(info[0], fg='yellow'))
    click.echo('疑似：' + click.style(info[1], fg='yellow'))
    click.echo('治愈：' + click.style(info[2], fg='yellow'))
    click.echo('死亡：' + click.style(info[3], fg='yellow'))


@click.command()
@click.option('-o', 'output_type', flag_value='o', help='Output the overall data of China')
@click.option('-d', 'output_type', flag_value='d', help='Output detailed data of all provinces and some cities')
@click.option('-a', 'output_type', flag_value='a', default=True, help='Output all data. overall --> detailed')
def main(output_type):

    """2019-nCoV is a new type of Coronavirus that originated in Wuhan, Hubei province, China.
    This is a battle of human civilization! As a human being, you should take your responsibility to protect yourself
    and other people around you!"""

    if output_type == 'a':
        click.clear()
        overall_report()
        click.echo()
        click.echo('Would You Like MORE Detailed Information? [Y/n]', nl=False)
        choice = click.getchar()
        click.echo()
        if choice == 'Y' or choice == 'y':
            detailed_info()
        elif choice == 'N' or choice == 'n':
            click.echo('OK, Fine. Have a Good Day! ')
        else:
            detailed_info()
    elif output_type == 'o':
        click.clear()
        overall_report()
        click.echo()
    elif output_type == 'd':
        detailed_info()


if __name__ == '__main__':
    main()
