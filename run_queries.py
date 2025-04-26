import kuzu

def run_query(conn, query) -> None:
    response = conn.execute(query)

    while response.has_next():
        print(response.get_next())


def main() -> None:
    # Create an empty on-disk database and connect to it
    db = kuzu.Database("./demo_db")
    conn = kuzu.Connection(db)

    run_query(conn,
        """
        MATCH (a:User)-[f:Follows]->(b:User)
        RETURN a.name, b.name, f.since;
        """
    )


if __name__ == '__main__':
    main()
