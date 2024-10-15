from pydantic import BaseModel, validator


class DateRequest(BaseModel):
    part: str
    
    @validator('part')
    def validate_part(cls, v):
        valid_parts = [
            'day_number',
            'day_name',
            'month_number',
            'month_name',
            'year'
        ]
        if v not in valid_parts:
            raise ValueError(f"Invalid part requested. Must be one of: {', '.join(valid_parts)}")
        return v


class DateTimeRequest(BaseModel):
    part: str
    
    @validator('part')
    def check_part(cls, v):
        valid_parts = [
            'date',
            'time',
            'day',
            'month',
            'year',
            'hour',
            'minute',
            'second',
            'both'
        ]
        if v not in valid_parts:
            raise ValueError(
                f"part must be one of: {', '.join(valid_parts)}")
        return v

