CREATE PROCEDURE dbo.PC_InserisciDisco
  @Title varchar(255),
  @Artist varchar(255),
  @Year int, 
  @Company varchar(50),
  @Id int OUT
AS

BEGIN
	INSERT INTO PC_Records 
		(Artist, Title, Company, [Year]) 
	VALUES 
		(@Artist, @Title, @Company, @Year) 
	
	SET @Id = SCOPE_IDENTITY()
END