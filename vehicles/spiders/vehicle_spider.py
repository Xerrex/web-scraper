import scrapy
from vehicles.items import VehicleItem

class VehicleSpider(scrapy.Spider):
    """Vehicle Spider to Fetch cars 
    """
    
    name = 'vehicle_spider'

    def start_requests(self):
        
        radius = getattr(self, 'radius', None)
        # zipcode =  getattr(self, 'zipcode', None) TODO: use  zipcode
        
        url = ""
        if radius is not None:
            url = f"https://www.edmunds.com/inventory/srp.html?inventorytype=used%2Ccpo&radius={radius}"
        else:
            url = "https://www.edmunds.com/cars-for-sale-by-owner/"
        
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        
        vehicles = response.xpath("//main/div[3]/div[1]/div[1]/div/ul/li")

        for vehicle in vehicles:
            vehicle_item = VehicleItem()

            vehicle_item["price"] = vehicle.xpath(".//div/div[2]/div/div[1]/div/span[1]/span/text()").get()
            vehicle_item["name"] = vehicle.xpath(".//div/div[2]/div/h2/a/text()").get()
            
            link_text = vehicle.xpath(".//div/div[2]/div/h2/a/@href").get()
            cb_kwargs = {
                "vehicle_item": vehicle_item
            }
            link = response.urljoin(link_text)
            yield scrapy.Request(link, callback=self.vehicle_parse, cb_kwargs=cb_kwargs)
    
    def vehicle_parse(self, response, vehicle_item):
        """Parse the vehicle details
        """
        vehicle = response.xpath("//main/div[1]/div[2]/div/div[1]")
        vehicle_item["vin_number"] = vehicle.xpath(".//div[2]/section/div[2]/div/span[1]/text()").getall()[1]
        vehicle_item["vehicle_summary"] = self.vehicle_summary_parser(vehicle)
        vehicle_item["top_features_specs"] = self.vehicle_top_features_and_specs(vehicle)

        return vehicle_item

    def vehicle_summary_parser(self, vehicle):

        """Parse the Vehicle Summary 
        
        fetch the items in the vehicle summary
        """

        vehicle_summary_section = vehicle.xpath("//div[3]/div[1]/div/section[1]")
        sections_of_vehicle_sum = vehicle_summary_section.xpath("./div/div")
        
        vehicle_summary = []

        for section in sections_of_vehicle_sum:
            section_items = section.xpath("./div")
            for section_item in section_items:
                section_item_data = section_item.xpath("./div[2]/text()").get()
                if not section_item_data:
                    section_item_data = section_item.xpath("./div[2]/span/text()").get()
                
                vehicle_summary.append(section_item_data)
        return vehicle_summary

    def vehicle_top_features_and_specs(self, vehicle):
        """Parse the Vehicle's Top Features & Specs
        
        vehicle = response.xpath("//main/div[1]/div[2]/div/div[1]")
        """
        
        top_ft_specs_section = vehicle.css(".features-and-specs")
        sections_of_top_ft_specs_section = top_ft_specs_section.xpath("./div[1]/div")

        top_features_and_specs = {}

        for section in sections_of_top_ft_specs_section:
            # get the title  
            section_title = section.xpath("./div[1]/text()").get()
            # get the features & specs
            section_ft_specs = section.xpath(".//div[2]/ul/li/text()").getall()
            top_features_and_specs[f"{section_title}"] = section_ft_specs

        return top_features_and_specs    