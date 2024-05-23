from fastapi import FastAPI, Response
from datetime import datetime, timedelta
from dbmodels import Emailreport
from MSDatabase import SessionLocal
import xlsxwriter
from io import BytesIO
import uvicorn


app = FastAPI()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

@app.get("/download_report")
async def download_report_and_send_email(email_address: str = None):

    seven_days_ago = datetime.now() - timedelta(days=7)
    session = SessionLocal()
    reports = session.query(
        Emailreport.email,
        Emailreport.created_at,
        Emailreport.name,
        Emailreport.title,
        Emailreport.organization
    ).filter(Emailreport.created_at >= seven_days_ago).all()

    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    worksheet = workbook.add_worksheet(name="Report")

    header_format = workbook.add_format({'bold': True, 'bg_color': '57A6A1'})
    headers = ['S.no.', 'Email', 'Created_at', 'Name', 'Title', 'Organization']

    default_col_width = 20
    worksheet.set_default_row(15)

    for col_num, header in enumerate(headers):
        worksheet.write(0, col_num, header, header_format)
        worksheet.set_column(col_num, col_num, default_col_width)

    for row_num, report in enumerate(reports, 1):
        worksheet.write(row_num, 0, row_num) 
        worksheet.write(row_num, 1, report.email)
        worksheet.write(row_num, 2, report.created_at)
        worksheet.write(row_num, 3, report.name)
        worksheet.write(row_num, 4, report.title)
        worksheet.write(row_num, 5, report.organization)

    workbook.close()
    output.seek(0)

    if email_address:
        try:
          
            await send_email_with_report(email_address, output.getvalue())
            return "Email sent successfully!"
        except Exception as e:
            return f"Error occurred while sending email: {str(e)}"
    else:
      
        return Response(content=output.getvalue(), media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers={
            "Content-Disposition": "attachment; filename=Weekly-Report.xlsx"
        })

async def send_email_with_report(email_address, attachment_data):
    
    sender_email = "ENTER YOUR EMAIL ID HERE"
    sender_password = " ENTER YOUR EMAIL PASSWORD HERE"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587  
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email_address
    message["Subject"] = "Weekly Report"
    email_body =""" <html>
    <body>
    <p>Hello,<br><br>
       Please find attached the Weekly Report.<br><br>
       This report provides an overview of the key metrics and performance indicators for the past week. 
       It includes detailed analyses of the following sections:
    </p>
    <ul>
        <li><strong>Sales Performance:</strong></li>
        <li><strong>Customer Engagement:</strong></li>
        <li><strong>Operational Efficiency:</strong></li>
        <li><strong>Market Trends:</strong></li>
    </ul>
    <p>We encourage you to review the report and reach out with any questions or feedback.<br><br>
       Best regards,<br>
       Your Name,<br>
    </p>
    </body>
    </html>"""



    message.attach(MIMEText(email_body, "html"))

    attachment = MIMEBase("application", "octet-stream")
    attachment.set_payload(attachment_data)
    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition",
        f"attachment; filename=Weekly-Report.xlsx",
    )
    message.attach(attachment)


    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, email_address, message.as_string())
    except Exception as e:
        raise e  




if __name__ == "__main__":
    uvicorn.run("reportmail:app", host="127.0.0.1", port=8000, reload=True)
