import click
import scrape
import download_webpage

@click.command()
@click.option('--url', help='Specify the URL to search for.', metavar='example.com')
@click.option('--term', help='Specify the search term.', metavar='"example"')
@click.option('--date', help='Specify a specific date.', metavar='YYYYMMDD')
@click.option('--time', help='Include the time in the search.', metavar='HHMMSS')
@click.option('--find', multiple=True, help='Find text on the webpage. (Case sensitive, include capitalization)', metavar='"Example"')
@click.option('--download', is_flag=True, help='Download webpage html.')
def main(url, term, date, time, find, download):
    """
    CLI program to interact with the wayback machine.
    """
    if not url and not term:
        click.echo("--url or --term is required to begin search.")
        return
    
    elif term and not url:
        click.echo(f"Searching for the term: {term}")
        response = scrape.scrape(term, 'New')
        scrape.termResults(response)
    
    elif url and not term:
        click.echo(f"Searching for the URL: {url}")
        response = scrape.scrape(url, 'New')
        info = scrape.getInfo(response)
        if info:
            print(info) 
            if date:
                if time and len(time) == 6:
                    snapshot_url = scrape.makeUrl(info, url, date, time)
                else:
                    snapshot_url = scrape.makeUrl(info, url, date, None)
                if download and find:
                    terms = [term.strip() for terms_tuple in find for term in terms_tuple.split(',')]
                    scrape.find(terms, snapshot_url)
                    print('')
                    download_webpage.savePage(snapshot_url, date)
                elif download and not find:
                    download_webpage.savePage(snapshot_url, date)
                elif not download and find:
                    terms = [term.strip() for terms_tuple in find for term in terms_tuple.split(',')]
                    scrape.find(terms, snapshot_url)
                else:
                    click.echo("Please specify an action. --find/--download")
                    return
            else:
                click.echo("Please specify a date. Use python main.py --help for more commands.")
                return
        else:
            click.echo("Invalid URL please try again.")
            return

    else:
        click.echo("Only one of the following options is allowed: --url --term")
        return

if __name__ == '__main__':
    main()
