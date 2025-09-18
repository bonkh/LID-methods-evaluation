import polars as pl

df = pl.scan_csv(
    "lid201-data.tsv.gz",
    sep="\t",
    has_header=False,
    new_columns=["text", "lang", "source"],
    infer_schema_length=1000,
)

print(df.select(pl.count()).collect())
