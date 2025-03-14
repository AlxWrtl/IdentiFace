import { Menu } from "lucide-react";
import { useState } from "react";
import { Link } from "react-router";
import { Button } from "~/components/ui/button";
import { Menubar, MenubarMenu, MenubarTrigger } from "~/components/ui/menubar";

export function NavBar() {
  const [MobileMenuOpen, setMobileMenuOpen] = useState(false);

  return (
    <Menubar className="flex sm:flex-row flex-col justify-between items-center shadow-none px-4 sm:px-8 py-3 sm:py-6 w-full">
      <div className="flex justify-between items-center w-full sm:w-auto">
        <div className="font-bold text-xl">
          <p>
            <Link to="/">IdentiFace</Link>
          </p>
        </div>
        <Button
          variant="ghost"
          className="sm:hidden"
          size="icon"
          onClick={() => setMobileMenuOpen(!MobileMenuOpen)}
        >
          <Menu className="w-6 h-6" />
        </Button>
      </div>
      {MobileMenuOpen && (
        <div className="sm:hidden z-10 flex flex-col space-y-4 bg-background py-4 w-full min-h-screen">
          <div className="flex flex-col gap-2">
            <Button variant="ghost" className="justify-start px-2 text-sm">
              <p>
                <Link to="/">About</Link>
              </p>
            </Button>
            <Button variant="ghost" className="justify-start px-2 text-sm">
              <p>
                <Link to="/Identifying">Identifying</Link>
              </p>
            </Button>
          </div>
          <div className="flex gap-2 mt-4 px-2 pt-4 border-t">
            <Button
              variant="outline"
              size="sm"
              className="flex-1"
              onClick={() => setMobileMenuOpen(!MobileMenuOpen)}
            >
              <p>
                <Link to="/signUp">Sign up</Link>
              </p>
            </Button>
            <Button
              variant="default"
              size="sm"
              className="flex-1"
              onClick={() => setMobileMenuOpen(!MobileMenuOpen)}
            >
              <p>
                <Link to="/login">Login</Link>
              </p>
            </Button>
          </div>
        </div>
      )}
      <div className="hidden md:flex items-center gap-2 bg-background">
        <MenubarMenu>
          <MenubarTrigger className="text-sm">
            <p>
              <Link to="/">About</Link>
            </p>
          </MenubarTrigger>
          <MenubarTrigger className="text-sm">
            <p>
              <Link to="/Identifying">Identifying</Link>
            </p>
          </MenubarTrigger>
        </MenubarMenu>
      </div>

      <div className="hidden sm:flex gap-2">
        <MenubarMenu>
          <Button variant="outline" size="sm" className="text-sm">
            <p>
              <Link to="/signUp">Sign up</Link>
            </p>
          </Button>
        </MenubarMenu>
        <MenubarMenu>
          <Button variant="default" size="sm" className="text-sm">
            <p>
              <Link to="/login">Login</Link>
            </p>
          </Button>
        </MenubarMenu>
      </div>
    </Menubar>
  );
}
