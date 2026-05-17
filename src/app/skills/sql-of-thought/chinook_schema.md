# Chinook Database Schema

## customers
- CustomerId INTEGER PRIMARY KEY
- FirstName NVARCHAR(40) NOT NULL
- LastName NVARCHAR(20) NOT NULL
- Company NVARCHAR(80)
- Address NVARCHAR(70)
- City NVARCHAR(40)
- State NVARCHAR(40)
- Country NVARCHAR(40)
- PostalCode NVARCHAR(10)
- Phone NVARCHAR(24)
- Fax NVARCHAR(24)
- Email NVARCHAR(60) NOT NULL
- SupportRepId INTEGER (FK -> employees.EmployeeId)

## invoices
- InvoiceId INTEGER PRIMARY KEY
- CustomerId INTEGER NOT NULL (FK -> customers.CustomerId)
- InvoiceDate DATETIME NOT NULL
- BillingAddress NVARCHAR(70)
- BillingCity NVARCHAR(40)
- BillingState NVARCHAR(40)
- BillingCountry NVARCHAR(40)
- BillingPostalCode NVARCHAR(10)
- Total NUMERIC(10,2) NOT NULL

## invoice_items
- InvoiceLineId INTEGER PRIMARY KEY
- InvoiceId INTEGER NOT NULL (FK -> invoices.InvoiceId)
- TrackId INTEGER NOT NULL (FK -> tracks.TrackId)
- UnitPrice NUMERIC(10,2) NOT NULL
- Quantity INTEGER NOT NULL

## tracks
- TrackId INTEGER PRIMARY KEY
- Name NVARCHAR(200) NOT NULL
- AlbumId INTEGER (FK -> albums.AlbumId)
- MediaTypeId INTEGER NOT NULL (FK -> media_types.MediaTypeId)
- GenreId INTEGER (FK -> genres.GenreId)
- Composer NVARCHAR(220)
- Milliseconds INTEGER NOT NULL
- Bytes INTEGER
- UnitPrice NUMERIC(10,2) NOT NULL

## genres
- GenreId INTEGER PRIMARY KEY
- Name NVARCHAR(120)

## albums
- AlbumId INTEGER PRIMARY KEY
- Title NVARCHAR(160) NOT NULL
- ArtistId INTEGER NOT NULL (FK -> artists.ArtistId)

## artists
- ArtistId INTEGER PRIMARY KEY
- Name NVARCHAR(120)

## media_types
- MediaTypeId INTEGER PRIMARY KEY
- Name NVARCHAR(120)

## playlists
- PlaylistId INTEGER PRIMARY KEY
- Name NVARCHAR(120)

## playlist_track
- PlaylistId INTEGER NOT NULL (FK -> playlists.PlaylistId)
- TrackId INTEGER NOT NULL (FK -> tracks.TrackId)
- PRIMARY KEY (PlaylistId, TrackId)

## employees
- EmployeeId INTEGER PRIMARY KEY
- LastName NVARCHAR(20) NOT NULL
- FirstName NVARCHAR(20) NOT NULL
- Title NVARCHAR(30)
- ReportsTo INTEGER (FK -> employees.EmployeeId)
- BirthDate DATETIME
- HireDate DATETIME
- Address NVARCHAR(70)
- City NVARCHAR(40)
- State NVARCHAR(40)
- Country NVARCHAR(40)
- PostalCode NVARCHAR(10)
- Phone NVARCHAR(24)
- Fax NVARCHAR(24)
- Email NVARCHAR(60)

## Key Relationships
- customers.SupportRepId -> employees.EmployeeId
- invoices.CustomerId -> customers.CustomerId
- invoice_items.InvoiceId -> invoices.InvoiceId
- invoice_items.TrackId -> tracks.TrackId
- tracks.AlbumId -> albums.AlbumId
- tracks.MediaTypeId -> media_types.MediaTypeId
- tracks.GenreId -> genres.GenreId
- albums.ArtistId -> artists.ArtistId
- playlist_track.PlaylistId -> playlists.PlaylistId
- playlist_track.TrackId -> tracks.TrackId
