import geopandas as gpd

in_file = '../gpkg/sample_data.gpkg' # sample file shared

# Read polygon and points layers
in_polys = gpd.read_file(in_file, layer='polygons')
in_points = gpd.read_file(in_file, layer='points')


# Find the points inside each polygon using sjoin()
point_in_polys = gpd.tools.sjoin(in_points, in_polys,
                                 predicate="within", how='left')
# Lambda function to get unique polygon names and aggreage with ','
lambda_fun = lambda x: ','.join(x.unique())
# Group points by index and aggregate polygon names
df = point_in_polys.groupby(point_in_polys.index).agg(lambda_fun)
# Find the number of points within each combination
df_pivot_table = df.pivot_table(columns=['name'], aggfunc='size')

print(df_pivot_table)
